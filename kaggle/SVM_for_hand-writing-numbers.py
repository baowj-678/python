from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report


digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=33)

#标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

#初始化SVM
lsvc = LinearSVC()
#进行训练
lsvc.fit(X_train, y_train)
#进行预测
y_predict = lsvc.predict(X_test)

print('The Accuracy of Linear SVC is', lsvc.score(X_test, y_test))

print(classification_report(y_test, y_predict, target_names=digits.target_names.astype(str)))
