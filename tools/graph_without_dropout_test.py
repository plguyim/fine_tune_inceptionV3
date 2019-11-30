from __future__ import print_function
from tensorflow.core.framework import graph_pb2
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('/tmp/data/', one_hot=True)


def display_nodes(nodes):
    for i, node in enumerate(nodes):
        print('%d %s %s' % (i, node.name, node.op))
        [print(u'└─── %d ─ %s' % (i, n)) for i, n in enumerate(node.input)]


def accuracy(predictions, labels):
    return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1)) / predictions.shape[0])


def test_graph(graph_path, use_dropout):
    tf.reset_default_graph()
    graph_def = tf.GraphDef()

    with tf.gfile.FastGFile(graph_path, 'rb') as f:
        graph_def.ParseFromString(f.read())

    _ = tf.import_graph_def(graph_def, name='')
    sess = tf.Session()
    prediction_tensor = sess.graph.get_tensor_by_name('final_result:0')

    feed_dict = {'input:0': mnist.test.images[:256]}
    if use_dropout:
        feed_dict['keep_prob:0'] = 1.0

    predictions = sess.run(prediction_tensor, feed_dict)
    result = accuracy(predictions, mnist.test.labels[:256])
    return result


graph = tf.GraphDef()
with tf.gfile.Open('./pb/optimized_frozen_graph.pb', 'rb') as f:
    data = f.read()
    graph.ParseFromString(data)

display_nodes(graph.node)


#InceptionV3/Logits/Dropout_1b/dropout/Shape -> InceptionV3/Logits/Dropout_1b/dropout/Cast

# 798 InceptionV3/Logits/Dropout_1b/dropout/Shape Shape
# └─── 0 ─ InceptionV3/Logits/AvgPool_1a_8x8/AvgPool

# 810 InceptionV3/Logits/Dropout_1b/dropout/mul Mul
# └─── 0 ─ InceptionV3/Logits/AvgPool_1a_8x8/AvgPool
# └─── 1 ─ InceptionV3/Logits/Dropout_1b/dropout/truediv
# 811 InceptionV3/Logits/Dropout_1b/dropout/Cast Cast
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/Shape

# 813 InceptionV3/Logits/Conv2d_1c_1x1/weights Const
# 814 InceptionV3/Logits/Conv2d_1c_1x1/biases Const
# 815 InceptionV3/Logits/Conv2d_1c_1x1/Conv2D Conv2D
# └─── 0 ─ InceptionV3/Logits/Dropout_1b/dropout/mul_1
# └─── 1 ─ InceptionV3/Logits/Conv2d_1c_1x1/weights
# 816 InceptionV3/Logits/Conv2d_1c_1x1/BiasAdd BiasAdd
# └─── 0 ─ InceptionV3/Logits/Conv2d_1c_1x1/Conv2D
# └─── 1 ─ InceptionV3/Logits/Conv2d_1c_1x1/biases
# 817 InceptionV3/Logits/SpatialSqueeze Squeeze
# └─── 0 ─ InceptionV3/Logits/Conv2d_1c_1x1/BiasAdd
# 818 InceptionV3/Predictions/Reshape/shape Const
# 819 InceptionV3/Predictions/Reshape Reshape
# └─── 0 ─ InceptionV3/Logits/SpatialSqueeze
# └─── 1 ─ InceptionV3/Predictions/Reshape/shape
# 820 InceptionV3/Predictions/Softmax Softmax
# └─── 0 ─ InceptionV3/Predictions/Reshape
# 821 InceptionV3/Predictions/Shape Shape
# └─── 0 ─ InceptionV3/Logits/SpatialSqueeze
# 822 InceptionV3/Predictions/Reshape_1 Reshape
# └─── 0 ─ InceptionV3/Predictions/Softmax
# └─── 1 ─ InceptionV3/Predictions/Shape

graph.node[812].input[0] = 'InceptionV3/Logits/AvgPool_1a_8x8/AvgPool'
graph.node[812].input[1] = 'InceptionV3/Logits/AvgPool_1a_8x8/AvgPool'
nodes = graph.node[:797] + graph.node[812:]

output_graph = graph_pb2.GraphDef()
output_graph.node.extend(nodes)

with tf.gfile.GFile('./pb/frozen_model_without_dropout.pb', 'w') as f:
    f.write(output_graph.SerializeToString())

# # Connect 'MatMul_1' with 'Relu_2'
# graph.node[44].input[0] = 'Relu_2' # 44 -> MatMul_1
# # Remove dropout nodes
# nodes = graph.node[:33] + graph.node[44:] # 33 -> MatMul_1
# del nodes[1] # 1 -> keep_prob
#
# # Save graph
# output_graph = graph_pb2.GraphDef()
# output_graph.node.extend(nodes)
# with tf.gfile.GFile('./pb/frozen_model_without_dropout.pb', 'w') as f:
#     f.write(output_graph.SerializeToString())

# test graph via simple test
# result_1 = test_graph('./freeze_graph.pb', use_dropout=True)
# result_2 = test_graph('./frozen_model_without_dropout.pb', use_dropout=False)

# print('with dropout:    %f' % result_1)
# print('without dropout: %f' % result_2)
