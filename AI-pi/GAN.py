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
        self.f2 = torch.nn.Linear(1024, 2)

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

def load_data():
    transformer = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ]
    )
    trainset = datasets.MNIST(root='./MNIST', train=True, transform=transformer, download=False)
    trainset.data = (trainset.data-127.5)/127.5
    return trainset

def train(BATCH_SIZE, G_LR, D_LR):
    print('ooooo')
    # get data
    dataset = load_data()
    traindata = dataset.data
    trainlabels = dataset.targets
    # testdata = dataset.test_data
    # testlabels = dataset.targets
    # get net
    generate_net = generate_Net(BATCH_SIZE)
    generate_optimizer = torch.optim.SGD(generate_net.parameters(), momentum=0.9, nesterov=True, lr=G_LR)
    generate_loss_func = torch.nn.CrossEntropyLoss()
    discriminator_net = discriminator_Net()
    discriminator_optimizer = torch.optim.SGD(discriminator_net.parameters(), momentum=0.9, nesterov=True, lr=D_LR)
    discriminator_loss_func = torch.nn.CrossEntropyLoss()
    # train
    for epoch in range(100):
        print('epoch is', epoch)
        for index in range(traindata.shape[0]//BATCH_SIZE):
            noise = torch.tensor(np.random.uniform(-1, 1, size=[BATCH_SIZE, 100]), dtype=torch.float32)
            image_batch = traindata[index*BATCH_SIZE : (index + 1)*BATCH_SIZE]
            # g_forward
            generate_images = generate_net.forward(noise)
            if (index % 20 == 0):
                pass
            # d_forward
            X = torch.cat((image_batch, generate_images), dim=0)
            y = torch.tensor([1]*BATCH_SIZE + [0]*BATCH_SIZE)
            X = torch.reshape(X, [-1, 1, 28, 28])
            discriminator_labels = discriminator_net.forward(X)
            # d_backward
            d_loss = discriminator_loss_func(discriminator_labels, y)
            print('batch %d d_loss : %.3f' % (index, d_loss))
            discriminator_optimizer.zero_grad()
            d_loss.backward()
            discriminator_optimizer.step()
            # train generate
            noise = torch.tensor(np.random.uniform(-1, 1, size=[BATCH_SIZE, 100]), dtype=torch.float32)
            generate_images = generate_net.forward(noise)
            generate_images = torch.reshape(generate_images, [-1, 1, 28, 28])
            discriminator_labels = discriminator_net.forward(generate_images)
            d_loss = generate_loss_func(discriminator_labels, torch.tensor([0]*BATCH_SIZE))
            generate_optimizer.zero_grad()
            d_loss.backward()
            generate_optimizer.step()
            print('batch %d g_loss : %.3f' % (index, d_loss))



# train(10, 0.0005, 0.0005)
for i in range(10000):
    print("he")