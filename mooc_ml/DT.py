from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

clf = DecisionTreeClassifier()
iris = load_iris()
print(cross_val_score(clf, iris.data, iris.target, cv=10))
