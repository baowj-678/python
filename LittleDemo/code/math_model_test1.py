import tensorflow as tf
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

TRAIN_RATE = 0.0001
File="C:/Users/Vilily/OneDrive/桌面/matlab.mat"
datas = sio.loadmat(File)
datas = np.array(datas['m'])
datas_max = np.sum(datas, 1)
datas_max = np.transpose(np.broadcast_to(datas_max, [335, 14]))
datas = datas / datas_max
datas = datas[:, np.newaxis, :]

x=np.linspace(1, 335, 335)
x = x[np.newaxis, :]
# for i in range(1):
#     plt.scatter(x, datas[i])
# plt.show()

y_ = tf.placeholder(tf.float32, [None, 335], 'target_y')
x_ = tf.placeholder(tf.float32, [1, 335])

w1 = tf.Variable(tf.random_normal([335, 335], mean=0.1))
b1 = tf.Variable(tf.random_normal([1, 335], mean=0.001), trainable=False)

w2 = tf.Variable(tf.random_normal([335, 335], mean=0.1))
b2 = tf.Variable(tf.random_normal([1, 335], mean=0.001), trainable=False)

w3 = tf.Variable(tf.random_normal([335, 335], mean=0.001))
b3 = tf.Variable(tf.random_normal([1, 335], mean=0.001), trainable=False)

w4 = tf.Variable(tf.random_normal([335, 335], mean=0.001))
b4 = tf.Variable(tf.random_normal([1, 335], mean=0.001), trainable=False)

w5 = tf.Variable(tf.random_normal([335, 335], mean=0.1))
b5 = tf.Variable(tf.random_normal([1, 335], mean=0.001), trainable=False)

w6 = tf.Variable(tf.random_normal([335, 335], mean=0.1))

h1 = tf.nn.relu(tf.matmul(x_, w1) + b1)
h2 = tf.nn.relu(tf.matmul(h1, w2) + b2)
h3 = tf.nn.relu(tf.matmul(h2, w3) + b3)
h4 = tf.nn.relu(tf.matmul(h3, w4) + b4)
h5 = tf.nn.relu(tf.matmul(h4, w5) + b5)

out = tf.nn.relu(tf.matmul(h5, w6))

loss = tf.reduce_mean(tf.math.square(y_ - out))

init = tf.global_variables_initializer()

train_step = tf.train.GradientDescentOptimizer(TRAIN_RATE).minimize(loss)

with tf.Session() as sess:
    sess.run(init)
    for i in range(1):
        sess.run(train_step, feed_dict={y_:datas[0], x_:x})
    out = sess.run(loss, feed_dict={y_:datas[0], x_:x})
    print(out)
    # plt.plot(x, out)
    # plt.show()


