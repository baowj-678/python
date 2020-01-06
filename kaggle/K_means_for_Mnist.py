import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics



digits_train = pd.read_csv('D:\\python\\vs_code\\python\\kaggle\\optdigits.tra',header=None)
digits_test = pd.read_csv('D:\\python\\vs_code\\python\\kaggle\\optdigits.tes',header=None)


X_train = digits_train[np.arange(64)]
y_train = digits_train[64]

X_test = digits_test[np.arange(64)]
y_test = digits_test[64]

kmeans = KMeans(n_clusters=10)
kmeans.fit(X_train)

y_pred = kmeans.predict(X_test)
print(y_pred.shape)
print(metrics.adjusted_mutual_info_score(y_test, y_pred))