# 由于神经网络训练数据集会非常大，用物理内存直接读取文件比较吃力，
# 所以将数据集转换成tfrecords文件, 方便读取

import tensorflow as tf
import numpy as np
import os
import glob
import math
from tensorflow.python.platform import gfile

import matplotlib.pyplot as plt

imagesFile = "/Users/admin/Documents/resource/images/flower_photos"
dataPath = "./data/"
imageSize = 299


def bytes_feature(value):
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(value=[value])
    )


def bytes_list_feature(aList):
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(value=aList)
    )


def int64_feature(value):
    return tf.train.Feature(
        int64_list=tf.train.Int64List(value=[value])
    )


def get_example(sess, imageFilePath, label):
    tf_image_raw_data = gfile.FastGFile(imageFilePath, 'rb').read()
    tf_image_data = tf.image.decode_jpeg(tf_image_raw_data)

    tf_image_data = sess.run(tf_image_data)
    shape = tf_image_data.shape
    image_height = shape[0]
    image_width = shape[1]
    image_deep = shape[2]

    features = tf.train.Features(feature={
        "image/data": bytes_feature(tf_image_raw_data),
        "image/height": int64_feature(image_height),
        "image/width": int64_feature(image_width),
        "image/deep": int64_feature(image_deep),
        "label": int64_feature(label)
    })

    example = tf.train.Example(features=features)
    serialized_example = example.SerializeToString()
    return serialized_example


def parse_example(example):
    features = tf.parse_single_example(example, features={
        "image/data": tf.FixedLenFeature([], tf.string),
        "image/height": tf.FixedLenFeature([], tf.int64),
        "image/width": tf.FixedLenFeature([], tf.int64),
        "image/deep": tf.FixedLenFeature([], tf.int64),
        "label": tf.FixedLenFeature([], tf.int64),
    })

    # image_height = tf.cast(features["image/height"], tf.int32)
    # image_width = tf.cast(features["image/width"], tf.int32)
    # image_deep = tf.cast(features["image/deep"], tf.int32)

    image = features["image/data"]
    image = tf.image.decode_jpeg(image)

    if image.dtype != tf.float32:
        image = tf.image.convert_image_dtype(image, tf.float32)

    # 将图片resize 299, 299, method=1的时候，接受uint8类型数据
    image = tf.image.resize_images(image, [imageSize, imageSize])

    # 设置resize之后的shape
    image = tf.reshape(image, [imageSize, imageSize, 3])

    label = tf.cast(features["label"], tf.int64)
    # label = features["label"]

    return image, label


# data == (imageName, label)
def save_data_to_files_as_tfrecord(sess, data, name):
    filename = os.path.join(dataPath, name + ".tfrecords")

    numberOfFiles = len(data)
    numberOfPerShard = 1000

    if numberOfFiles < numberOfPerShard:
        writer = tf.python_io.TFRecordWriter(filename)
        for (image, label) in data:
            writer.write(get_example(sess, image, label))
        writer.close()

    else:
        index = 0
        numberOfShards = math.ceil(numberOfFiles / numberOfPerShard)

        for (image, label) in data:
            if index % numberOfPerShard == 0:
                end = min(index + numberOfPerShard - 1, numberOfFiles)
                filePath = ('%s-%.5d-of-%.5d' % (filename, index, end))
                print(filePath)
                writer = tf.python_io.TFRecordWriter(filePath)

            writer.write(get_example(sess, image, label))

            if index == numberOfFiles or index % numberOfPerShard == numberOfPerShard-1:
                writer.close()

            index += 1

    print("finished creating %s." % filename)


def create_data_as_tfrecords():
    if not os.path.exists(dataPath):
        os.mkdir(dataPath)

    subDirs = [x[0] for x in os.walk(imagesFile)]
    if len(subDirs) > 0:
        subDirs.pop(0)

    label = 0

    trainDataInfos = []
    testDataInfos = []

    with open("./data/label.txt", "w") as f:
        # 遍历图片类各子目录，并附加标签
        for dir in subDirs:

            # 记录标签号和标签名
            f.write(str(label) + "," + os.path.basename(dir) + "\n")

            imageNames = glob.glob(os.path.join(dir, "*.jpg"))

            for imageName in imageNames:

                # 随机数
                chance = np.random.randint(100)
                data = (imageName, label)

                if chance < 10:
                    testDataInfos.append(data)
                else:
                    trainDataInfos.append(data)

            label += 1

    print("train files has %d" % len(trainDataInfos))
    print("test files has %d" % len(testDataInfos))

    with tf.Session() as sess:

        # 训练数据集
        save_data_to_files_as_tfrecord(sess, trainDataInfos, "train")

        # 验证数据集
        save_data_to_files_as_tfrecord(sess, testDataInfos, "test")


# 解析图片
def test_show_image():
    # 调用"tf.train.match_filenames_once"，使用前需要tf.local_variables_initializer()初始化参数
    files = tf.train.match_filenames_once('./data/test.*')
    filename_queue = tf.train.string_input_producer(files, shuffle=False)

    reader = tf.TFRecordReader()
    _, example = reader.read(filename_queue)
    tf_image, tf_label = parse_example(example)

    with tf.Session() as sess:
        sess.run([tf.local_variables_initializer()])

        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord, sess=sess)

        for i in range(10):
            image, label = sess.run([tf_image, tf_label])

            print(image)
            print(label)
            print(image.shape)
            plt.imshow(image)
            plt.show()

        coord.request_stop()
        coord.join(threads)


def main(argv=None):
    # test_show_image()
    create_data_as_tfrecords()


if __name__ == '__main__':
    tf.app.run()


