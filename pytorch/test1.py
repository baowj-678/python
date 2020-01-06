import torch
import numpy as np
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.optim as optim

LEARNING_RATE = 0.000003
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.f1 = nn.Linear(1, 2)
        self.f2 = nn.Linear(2, 4)
        self.f3 = nn.Linear(4, 8)
        self.f4 = nn.Linear(8, 4)
        self.f5 = nn.Linear(4, 2)
        self.f6 = nn.Linear(2, 1)

    def forward(self, x):
        x = torch.relu(self.f1(x))
        x = self.f2(x)
        x = self.f3(x)
        x = self.f4(x)
        x = self.f5(x)
        x = self.f6(x)
        return x

net = Net()
X = torch.linspace(0, 10, 100, dtype=torch.float).view([-1, 1])
Y = 5*X*X
Y = Y.view([-1, 1])

optimzer = optim.SGD(net.parameters(), lr=LEARNING_RATE)
criterion = nn.MSELoss()

print("before")
print(net.f1.weight, net.f2.weight)

for i in range(10):
    for j in range(100):
        input_ = X[j]
        target = Y[j]
        optimzer.zero_grad()
        output = net(input_)
        loss = criterion(output, target)
        loss.backward()
        optimzer.step()

Y_pred = torch.zeros(Y.size()[0])
for i in range(X.size()[0]):
    Y_pred[i] = net(X[i])

print('after')
print(net.f1.weight, net.f2.weight)
plt.scatter(X, Y)
plt.scatter(X, Y_pred.detach().numpy())
plt.show()