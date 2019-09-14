from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import graphviz

wine = load_wine()

# print(wine.target)

# import pandas as pd
# print(pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)], axis=1))

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
# print(Xtarin.shape)
# print(wine.data.shape)

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)
print(score)

dot_data = tree.export_graphviz(clf, 
                                feature_names=wine.feature_names, 
                                class_names=["0","1","2"],
                                filled=True,
                                rounded=True)

graph = graphviz.Source(dot_data)
graph