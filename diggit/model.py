#encode=utf-8

import tensorflow as tf
from diggit.load_data import deal_train_data

def net(input):
    dens1 = tf.layers.dense(inputs=input,
                            units=512,
                            activation=tf.nn.relu)
    dens2 = tf.layers.dense(inputs=dens1,
                            units=256,
                            activation=tf.nn.relu)

    dens3 = tf.layers.dense(inputs=dens2,
                            units=128,
                            activation=tf.nn.relu)

    dens4 = tf.layers.dense(inputs=dens3,
                            units=10,
                            activation=tf.nn.relu)
    return dens4

def loss(x, y):
    logit = net(x)
    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logit, labels=tf.arg_max(y, 1))
    loss = tf.reduce_mean(loss)
    train_step = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)
    return loss, train_step


def train():
    x = tf.placeholder(tf.float32, [None, 784])
    y = tf.placeholder(tf.float32, [None, 1])
    btch = 64
    losses, train_step= loss(x, y)
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        for i in range(100):
            data, lable = deal_train_data(i*btch, (i + 1) * btch)
            los, _ = sess.run([losses, train_step], feed_dict={x: data, y: lable})
            print(los)




if __name__ == '__main__':
    train(2500, 600)