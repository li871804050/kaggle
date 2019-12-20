import tensorflow as tf

#先用word2vec 训练词向量模型 解决单词的表示
#1*16


def testCNN():
    input_x = tf.placeholder(tf.int32, [1, 16], name="input_x")
    input_y = tf.placeholder(tf.float32, [1, 1], name="input_y")

    conv1 = tf.layers.conv2d(inputs= input_x, )