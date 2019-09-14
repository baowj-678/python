import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.metrics import classification_report


column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion'
                    ,'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
def get_data():
    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', names=column_names)

    data = data.replace(to_replace='?', value=np.nan)

    data = data.dropna(how='any')

    return data

def train_data(data):
    X_train, X_test, y_train, y_test = train_test_split(data[column_names[1:10]], data[column_names[10]], test_size=0.25, random_state=33)
    ss = StandardScaler()
    #标准化数据
    X_train = ss.fit_transform(X_train)
    X_test = ss.transform(X_test)
    print(y_train.value_counts())
    print(y_test.value_counts())
    lr = LogisticRegression()
    sgdc = SGDClassifier()
    #训练模型
    lr.fit(X_train, y_train)
    #利用模型预测
    lr_y_predict = lr.predict(X_test)
    #训练模型
    sgdc.fit(X_train, y_train)
    #预测
    sgdc_y_predict = sgdc.predict(X_test)

    #report
    print('Accuracy of LR Classifier:', lr.score(X_test, y_test))
    print(classification_report(y_test, lr_y_predict, target_names=['Benign', 'Malignant']))
    print('Accuracy of SGD Classifier:', sgdc.score(X_test, y_test))
    print(classification_report(y_test, sgdc_y_predict, target_names=['Benign', 'Malignant']))



def main():
    data = get_data()
    train_data(data)


main()