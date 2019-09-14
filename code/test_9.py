import tensorflow as tf
import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt

data0=scio.loadmat("D:\matlab.mat")
data=np.array(data0['m'],dtype=np.float32)
data_=np.zeros([data.shape[0],150])
for i in range(data.shape[0]):
    data_[i]=data[i,:150]/np.max(data[i])*10
x=np.linspace(1.0,150.0,150)[:,np.newaxis]
print(x)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(x,np.transpose(data_[13]))
plt.ion()
plt.show()
plt.pause(3)


x_=tf.convert_to_tensor(x,dtype=tf.float32)
y_=tf.placeholder(tf.float32,[150,1])

w1=tf.Variable(tf.random_normal([1,30],9))
w2=tf.Variable(tf.random_normal([30,30],1))
w3=tf.Variable(tf.random_normal([30,10],10))
w4=tf.Variable(tf.random_normal([10,30],8))

w5=tf.Variable(tf.random_normal([30,1],3))

y=tf.nn.relu(tf.matmul(x_,w1))
y=tf.nn.tanh(tf.matmul(y,w2))
y=tf.nn.sigmoid(tf.matmul(y,w3))
y=tf.nn.tanh(tf.matmul(y,w4))
y=tf.nn.tanh(tf.matmul(y,w5))
t=1
loss=tf.reduce_mean(tf.square(y-y_)*t)

train_step=tf.train.GradientDescentOptimizer(0.9).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        for j in range(10):
            y1=np.transpose(data_[j])[:,np.newaxis]
            sess.run(train_step,feed_dict={y_:y1})
            if(j==1):
                try:
                    ax.lines.remove(lines[0])
                except:
                    pass
                l=sess.run(loss,feed_dict={y_:np.transpose(data_[13])[:,np.newaxis]})
                if(l<0.01 and t<10e10):
                    t=t*10
                    print(t)
                print(l)
                #print(sess.run(y,feed_dict={y_:np.transpose(data[13])[:,np.newaxis]}))
                
                prediction=np.array(sess.run(y,feed_dict={y_:np.transpose(data_[13])[:,np.newaxis]}))
                lines=ax.plot(x,prediction,'r-',lw=5)
                plt.pause(0.2)
    plt.pause(10)

