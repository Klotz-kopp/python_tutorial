#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


df = sns.load_dataset("penguins")
df = df.dropna()
df = df.drop(["island", "sex"], axis = 1)
X = df.drop(["species"], axis = 1)
y = df["species"]
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 119)
clf = KNeighborsClassifier(n_neighbors = 3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print(accuracy_score(predictions, y_test))