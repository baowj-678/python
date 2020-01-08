import torch
import numpy as np
from torchvision import datasets, transforms

class generate_Net(torch.nn.Module):
    def __init__(self, BATCH_SIZE):
        super(generate_Net, self).__init__()
        self.BATCH_SIZE = BATCH_SIZE
        self.f1 = torch.nn.Linear(100, 1024)
        self.f2 = torch.nn.Linear(1024, 128*7*7)
        self.BN1 = torch.nn.BatchNorm1d(128*7*7)
        self.UpS1 = torch.nn.Upsample(size=(14, 14))
        self.conv1 = torch.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=(5, 5), padding=2)
        self.UpS2 = torch.nn.Upsample(size=(28, 28))
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=(5, 5), padding=2)

    def forward(self, x):
        x = torch.relu(self.f1(x))
        x = self.f2(x)
        x = self.BN1(x)
        x = torch.relu(x)
        x = torch.reshape(x, [-1, 128, 7, 7])
        x = self.UpS1(x)
        x = self.conv1(x)
        x = torch.relu(x)
        x = self.UpS2(x)
        x = self.conv2(x)
        x = torch.tanh(x)
        x = torch.reshape(x, [-1, 28, 28])
        return x


class discriminator_Net(torch.nn.Module):
    def __init__(self):
        super(discriminator_Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=64, kernel_size=(5, 5), padding=2)
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(5, 5), padding=2)
        self.f1 = torch.nn.Linear(7*7*128, 1024)
        self.f2 = torch.nn.Linear(1024, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = torch.tanh(x)
        x = torch.max_pool2d(x, kernel_size=(2, 2))
        x = self.conv2(x)
        x = torch.tanh(x)
        x = torch.max_pool2d(x, kernel_size=(2, 2))
        x = torch.flatten(x, start_dim=1)
        x = self.f1(x)
        x = torch.tanh(x)
        x = self.f2(x)
        x = torch.sigmoid(x)
        return x

def conbine_images(generate_images):
    num = generate_images.shape[0]
    width = int(ma)
def train(BATCH_SIZE):
    # generate_net = generate_Net(BATCH_SIZE)
    # x_train = np.random.uniform(size=[BATCH_SIZE, 100])
    # x_train = torch.tensor(x_train, dtype=torch.float32)
    # print(generate_net.forward(x_train))
    x_train = np.random.uniform(size=[1, 1, 28, 28])
    x_train = torch.tensor(x_train, dtype=torch.float32)
    discriminator_net = discriminator_Net()
    print(discriminator_net.forward(x_train))



train(2)