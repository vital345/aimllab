from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

iris = load_iris()
kn = KNeighborsClassifier(n_neightbors=3)
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
kn.fit(X_train, y_train)
y_predict = kn.predict(X_test)

confusion_matrix(y_test, y_predict)
