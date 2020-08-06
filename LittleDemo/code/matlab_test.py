import tensorflow as tf
import matplotlib.pyplot as plt
import scipy.io as scio
import numpy as np

data0=scio.loadmat('D:\matlab.mat')
data=np.array(data0['m'],dtype=np.float32)

for i in range(14):
    data[i]=data[i]/np.max(data[i])

x=np.linspace(1.,3.,335,dtype=np.float32)[np.newaxis,:]

y_=tf.placeholder(tf.float32,[None,335])
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(x,data[13])
plt.ion()
plt.show()
plt.pause(3)

w1=tf.Variable(tf.random_uniform([335,30],0.001))
w2=tf.Variable(tf.random_uniform([30,335],0,0.01))

biases=tf.Variable(tf.random_uniform([1,30],-0.001,0.001),trainable=False)

y1=tf.nn.softmax(tf.matmul(x,w1))
y2=tf.nn.softmax(tf.matmul(y1,w2))

loss=tf.reduce_mean(tf.square(y_-y2))

train_step=tf.train.GradientDescentOptimizer(0.0000001).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(10):
        for j in range(13):
            sess.run(train_step,feed_dict={y_:data[j][np.newaxis,:]})
            if(j==1):
                prediction=sess.run(y2,feed_dict={y_:data[13][np.newaxis,:]})
                print(prediction)
                lines=ax.plot(x,prediction,'r-',lw=5)
                plt.pause(0.1)
                print(sess.run(loss,feed_dict={y_:data[13][np.newaxis,:]}))

