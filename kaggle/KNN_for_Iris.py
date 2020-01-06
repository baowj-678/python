# 导入数据标准化模块
from sklearn.preprocessing import StandardScaler
# 导入k近邻分类器
from sklearn.neighbors import KNeighborsClassifier
# 导入iris数据加载器
from sklearn.datasets import load_iris
# 导入数据分割模块
from sklearn.model_selection import train_test_split
import numpy as np


iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=33)

# 对训练数据进行标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

knc = KNeighborsClassifier()
knc.fit(X_train, y_train)
y_predict = knc.predict(X_test)

print(y_predict)
print(y_test)
print(np.sum(y_predict == y_test)/y_test.shape[0])