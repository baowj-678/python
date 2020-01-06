import torchvision.datasets as datasets
from sklearn.cluster import KMeans
import torch.transforms as transforms
import numpy as np

train_data = datasets.MNIST(root='/mnist', train=True, transform=transforms.ToTensor(), download=False)
test_data = datasets.MNIST(root='/mnist', train=False, transform=transforms.ToTensor(), download=False)

X_train = train_data.data

