import numpy as np
import matplotlib.pyplot as plt


class Net():
    def __init__(self):
        self.batch_num = 1
        self.learning_rate = 0.0000001
        self.three = 1
        self.two = 1
        self.one = 1

    def forward(self, i):
        self.last_x = self.X[i]
        self.f11 = self.three*self.X[i*self.batch_num:(i+1)*self.batch_num, ]**3
        self.f12 = self.two*self.X[i*self.batch_num:(i+1)*self.batch_num, ]**2
        self.f13 = self.one*self.X[i*self.batch_num:(i+1)*self.batch_num, ]
        self.out = self.f11 + self.f12 + self.f13
        self.loss = -(self.out - self.Y[i*self.batch_num:(i+1)*self.batch_num, ])/self.batch_num
        # print(self.out, self.Y[i], self.loss)
    def backward(self):
        self.three = self.three + self.last_x**3*self.loss*self.learning_rate
        self.two = self.two + self.last_x**2*self.loss*self.learning_rate
        self.one = self.one + self.last_x*self.loss*self.learning_rate
        # print("parament",self.three, self.two, self.one)


    def train(self, X, Y):
        self.X = X
        self.Y = Y
        self.num = X.shape[0]
        self.batch = self.num // self.batch_num
        for j in range(10):
            for i in range(self.batch):
                self.forward(i)
                self.backward()
            print(self.loss)
        self.draw()

    def draw(self):
        print("lass:", self.loss)
        print(self.three, self.two, self.one)
        plt.plot(self.X, self.three*self.X**3 + self.two*self.X**2 + self.one*self.X, color='red')
        plt.scatter(self.X, self.Y)
        plt.show()


x = np.linspace(-10, 10, num=100)
y = 0.3*x**3 + x**2 + 9*x + np.random.normal(0, 100, (100))
# plt.plot(x, y)
# plt.show()
net = Net()
net.train(x, y)
