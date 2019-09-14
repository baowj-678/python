import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import scipy.io as scio


def add_layer(inputs,in_size,out_size,activation_function=None):            #隐藏层
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.001)
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

data0=scio.loadmat('D:\matlab.mat')
data=np.array(data0['m'],dtype=np.float32)
data[0]=data[0]/np.max(data[0])

x_data=np.linspace(0,0.1,335,dtype=np.float32)[:,np.newaxis]
y_data=data

xs=x_data
ys=tf.placeholder(tf.float32,[None,1])

l1=add_layer(xs,1,30,activation_function=tf.nn.relu)     #输入层

prediction=add_layer(l1,30,1,activation_function=tf.nn.relu)

loss=tf.reduce_mean(tf.square((ys-prediction)))

train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(x_data,data[0][:,np.newaxis])
    plt.ion()
    plt.show()

    for i in range(6000):
        sess.run(train_step,feed_dict={ys:y_data[0][:,np.newaxis]})
        if i%50==0:
            try:
                ax.lines.remove(lines[0])
            except:
                pass
            prediction_value=sess.run(prediction)
            lines=ax.plot(x_data,prediction_value,'r-',lw=5)
            plt.pause(0.1)
            temp=sess.run(loss,feed_dict={ys:y_data[0][:,np.newaxis]})
            print(temp)