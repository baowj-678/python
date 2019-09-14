import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def add_layer(inputs,in_size,out_size,activation_function=None):            #隐藏层
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

x_data=np.linspace(-10,10,300)[:,np.newaxis]
noise=np.random.normal(0,0.6,x_data.shape)
y_data=np.cos(x_data)*x_data/3-0.5+noise
t1=1000
t2=1
print(x_data.shape)
xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])

l1=add_layer(xs,1,10,activation_function=tf.nn.tanh)     #输入层

l2=add_layer(l1,10,40,activation_function=tf.nn.tanh)

l3=add_layer(l2,40,30,activation_function=tf.nn.sigmoid)#sigmoid

l4=add_layer(l3,30,30,activation_function=tf.nn.relu)#relu

prediction=add_layer(l4,30,1,activation_function=None)

loss=tf.reduce_sum(tf.reduce_sum(tf.square((ys-prediction)*t2/t1),reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(x_data,y_data)
    plt.ion()
    plt.axis([-11,11,-20,20])
    plt.show()

    for i in range(600000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i%500==0:
            try:
                ax.lines.remove(lines[0])
            except:
                pass
            prediction_value=sess.run(prediction,feed_dict={xs:x_data})
            lines=ax.plot(x_data,prediction_value,'r-',lw=5)
            plt.pause(0.1)
            temp=sess.run(loss,feed_dict={xs:x_data,ys:y_data})

            if temp<0.001 and t2<10e10:
                t2*=10
            print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))

