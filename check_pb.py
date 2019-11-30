import tensorflow as tf
from tensorflow.python.platform import gfile

# model = 'pb/frozen_model_without_dropout.pb'
model = 'pb/optimized_frozen_graph.pb'
# model = 'pb/freeze_graph.pb'
# model = 'export_dir/1574975499/saved_model.pb'
graph = tf.get_default_graph()
graph_def = graph.as_graph_def()
graph_def.ParseFromString(gfile.FastGFile(model, 'rb').read())
tf.import_graph_def(graph_def, name='InceptionV3_finetune')
summaryWriter = tf.summary.FileWriter('log/', graph)


# 在"log/..."生成了log文件, 再使用tensorboard命令去读取模型