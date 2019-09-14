from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
import numpy as np


boston = load_boston()
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)

# print(np.max(boston.target))
# print(np.min(boston.target))
# print(np.mean(boston.target))
#对数据进行标准化
ss_X = StandardScaler()
ss_y = StandardScaler()
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train.reshape(-1,1))
y_test = ss_y.transform(y_test.reshape(-1,1))
y_train = np.ravel(y_train)
y_test = np.ravel(y_test)
#线性回归LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_y_pred = lr.predict(X_test)
print("线性回归器：",lr.score(X_test, y_test))
#线性回归器SGDRegression
sgdr = SGDRegressor()
sgdr.fit(X_train, y_train)
sgdr_y_pred = sgdr.predict(X_test)
print("SGD:",sgdr.score(X_test, y_test))
