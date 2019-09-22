import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

X['age'].fillna(X['age'].mean(), inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
vec = DictVectorizer(sparse=False)
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc_y_pred = dtc.predict(X_test)

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
rfc_y_pred = rfc.predict(X_test)

gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)
gbc_y_pred = gbc.predict(X_test)

print('The accuracy of decision tree is:',dtc.score(X_test, y_test))
print(classification_report(dtc_y_pred, y_test))

print('The accuracy of random forest classifier is:',rfc.score(X_test, y_test))
print(classification_report(rfc_y_pred, y_test))

print('The accuracy of gradient tree boosting is:',gbc.score(X_test, y_test))
print(classification_report(gbc_y_pred, y_test))

