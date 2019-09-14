from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

news = fetch_20newsgroups(subset='all')
#数据分类
X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)
vec = CountVectorizer()
#训练贝叶斯模型
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)
#模型评估
mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_predict = mnb.predict(X_test)
#打印模型信息
print(mnb.score(X_test, y_test))
print(classification_report(y_test, y_predict, target_names=news.target_names))


#训练支持向量机模型
lsvc = LinearSVC()
lsvc.fit(X_train, y_train)
y_predict_lsvc = lsvc.predict(X_test)
print("lsvc:", lsvc.score(X_test, y_test))
print(classification_report(y_test, y_predict_lsvc, target_names=news.target_names))