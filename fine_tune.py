import tensorflow as tf
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.python.slim.nets.inception_v3 as inception_v3
from tensorflow.python.compiler import tensorrt as trt

from tensorflow.python.tools import freeze_graph
from google.protobuf import text_format
# from tf.contrib.lite import  convert_savedmodel

import glob
import transform_data as td



# 谷歌已经训练好的inception_v3.ckpt文件路径
INCEPTION_V3_PATH = "/Users/admin/Documents/Resource/models/inception_v3.ckpt"

LEARNING_RATE = 0.001

NUM_CLASSES = 5

# 不需要从谷歌训练好的模型中加载的参数。这里就是最后的全连接层，因为在
# 新的问题中要重新训练这一层中的参数。这里给出的是参数的前缀。
CHECKPOINT_EXCLUDE_SCOPES = 'InceptionV3/Logits,InceptionV3/AuxLogits'

# 需要训练的网络层参数名称，在fine-tuning的过程中就是最后的全连接层。
# 这里给出的是参数的前缀。
TRAINABLE_SCOPE = CHECKPOINT_EXCLUDE_SCOPES


def input_fn(files, batch_size, repeat=False):
    dataset = tf.data.TFRecordDataset(files)
    dataset = dataset.map(lambda x: td.parse_example(x))
    dataset = dataset.shuffle(buffer_size=1024).batch(batch_size)

    if repeat:
        dataset = dataset.repeat()

    iterator = dataset.make_one_shot_iterator()
    batch_images, batch_labels = iterator.get_next()
    return batch_images, batch_labels


# 获取所有需要从谷歌训练好的模型中加载的参数。(过滤掉最后的全连接层的所有参数名)
def get_tuned_variables():
    exclusions = [scope.strip() for scope in CHECKPOINT_EXCLUDE_SCOPES.split(',')]

    variables_to_restore = []
    # 枚举inception-v3模型中所有的参数，然后判断是否需要从加载列表中移除。
    for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
            if var.op.name.startswith(exclusion):
                excluded = True
                break
        if not excluded:
            variables_to_restore.append(var)

    return variables_to_restore


# 获取所有需要训练的变量列表(获取最后的全连接层的参数名)
def get_trainable_variables():
    # 好像用不到，因为要进行fine_tune操作，要排除掉原来的全连接层
    scopes = [scope.strip() for scope in TRAINABLE_SCOPE.split(',')]

    variables_to_train = []

    # 枚举所有需要训练的参数前缀，遍历查找前缀为scope的所有参数。
    for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variables_to_train.extend(variables)

    return variables_to_train


def model_fn(features, labels, mode, params=None):

    # 定义inputs节点
    # features = tf.identity(features, name="input_tensor")
    is_training = (mode == tf.estimator.ModeKeys.TRAIN)

    # 获取非Train下的checkpoint
    # is_training = True

    if isinstance(features, dict):
        features = features['feature']

    # batch_norm_decay,这个数值越大，网络训练越平缓, 小数据集可适设小点; 测试集正确率是否会上升?
    with slim.arg_scope(inception_v3.inception_v3_arg_scope(batch_norm_decay=0.88)):
        # inception_v3模型参数进行过normalize_batch，is_training为false会导致命中降低
        logits, _ = inception_v3.inception_v3(inputs=features,
                                              num_classes=NUM_CLASSES,
                                              is_training=is_training,
                                              )

        # logits = tf.identity(logits, name="output_tensor")

    if mode == tf.estimator.ModeKeys.PREDICT:
        # 定义output节点
        return tf.estimator.EstimatorSpec(
            mode=mode,
            predictions=tf.argmax(logits, 1, name="predictions"),
            # scaffold=scaffold
        )

    eval_metric_ops = {
        "my_metric": tf.metrics.accuracy(tf.argmax(logits, 1), labels)
    }

    # trainable_variables = get_trainable_variables()

    # 获取需要微调的参数名
    tuned_variables = get_tuned_variables()

    # 定义交叉熵损失。注意在模型定义的时候已经将正则化损失加入损失集合了。
    tf.losses.softmax_cross_entropy(tf.one_hot(labels, NUM_CLASSES), logits, weights=1.0)

    loss = tf.losses.get_total_loss()

    if mode == tf.estimator.ModeKeys.TRAIN:
        # 添加TensorBoard
        tf.summary.scalar('train_loss', loss)

        correct_predication = tf.equal(tf.argmax(logits, 1), labels)
        train_acc = tf.reduce_mean(tf.cast(correct_predication, tf.float32))
        tf.summary.scalar('train_acc', train_acc)

    # scaffold在estimator参数中用于初始化参数，读取save点等
    init_fn = slim.assign_from_checkpoint_fn(INCEPTION_V3_PATH, tuned_variables, ignore_missing_vars=True)
    scaffold = tf.train.Scaffold(init_fn=lambda s, sess: init_fn(sess))

    # 定义训练过程。之类minimize的过程中指定了需要优化的变量集合。
    optimizer = tf.train.RMSPropOptimizer(learning_rate=LEARNING_RATE)

    with slim.arg_scope(inception_v3.inception_v3_arg_scope()):
        # !!!!:解决batchNorm层的问题, moving_mean和moving_variance加入到ops.GraphKeys.UPDATE_OPS
        # 这地方被坑了太久了!!
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies([tf.group(*update_ops)]):
            train_op = optimizer.minimize(loss=loss, global_step=tf.train.get_global_step())

    return tf.estimator.EstimatorSpec(
        mode=mode,
        loss=loss,
        train_op=train_op,
        eval_metric_ops=eval_metric_ops,
        scaffold=scaffold
    )


def save_model():
    def receive_fn():
        features = tf.placeholder(dtype=tf.float32,
                                  shape=[1, 299, 299, 3],
                                  name='input_tensor')

        return tf.estimator.export.ServingInputReceiver(features, features)

    estimator = tf.estimator.Estimator(
        model_fn=model_fn,
        model_dir="./train_model/"
    )

    estimator.export_saved_model('./export_dir/', receive_fn)


def train(steps=50):
    estimator = tf.estimator.Estimator(
        model_fn=model_fn,
        model_dir="./train_model/"
    )

    train_files = glob.glob("./data/train.*")

    estimator.train(input_fn=lambda: input_fn(train_files, batch_size=32, repeat=True),
                    steps=steps)
    print("########### train opt finish. ############")


def evaluate():
    print("########### begin evaluate. ############")

    estimator = tf.estimator.Estimator(
        model_fn=model_fn,
        model_dir="./train_model/"
    )

    test_files = glob.glob("./data/test.*")

    result = estimator.evaluate(input_fn=lambda: input_fn(test_files, batch_size=128))

    accuracy_score = result["my_metric"]
    print("\nTest accuracy: %g %%" % (accuracy_score * 100))


def predication():
    print("########### begin predication. ############")

    estimator = tf.estimator.Estimator(
        model_fn=model_fn,
        model_dir="./train_model/"
    )

    batch_size = 64
    test_files = glob.glob("./data/test.*")

    predications = estimator.predict(input_fn=lambda: input_fn(test_files, batch_size=batch_size))
    print(','.join([str(x) for x in predications]))


# 打印所有node节点
def print_all_graph_node_names():
    with open('./train_model/graph.pbtxt') as f:
        graph_def = text_format.Parse(f.read(), tf.GraphDef())

    print([n.name for n in graph_def.node])


def main(argv=None):
    # train(600)
    # evaluate()
    predication()
    # save_model()


if __name__ == '__main__':
    tf.app.run()
