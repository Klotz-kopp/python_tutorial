#  Copyright (c) 2025. Diese Python Skripte wurden von mir erstellt und können als Referenz von anderen genutzt und gelesen werden.
import seaborn as sns
from funktionen import printf
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataframe definieren
df = sns.load_dataset("penguins")
# Null-Zeilen entfernen
df = df.dropna()
# nicht numerische Zeilen entfernen
df = df.drop(["island", "sex"], axis=1)
# Features definiert
X = df.drop(["species"], axis=1)
# Labels definiert
y = df["species"]
# Dataframe in Test und Trainingsdaten aufgeteilt
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=119)
# Wir prüfen die Genauigkeit der Vorhersagen mit 1-10 Nachbarn
genauigkeitswerte = []
for i in range(1, 11):
    # Classifier definiert
    clf = KNeighborsClassifier(n_neighbors=i)
    # Classifier mit Trainingsdaten traininert
    clf.fit(X_train, y_train)
    # Vorhersagen mit dem Classifier auf die Testdaten durchgeführt
    predictions = clf.predict(X_test)
    # Vorhersagegenauigkeit berechnet, indem die Vorhersagen mit der realität verglichen wurde
    printf(
        f"Bei der Verwendung des Wert {i} erreichen wir eine Genauigkeit von {accuracy_score(predictions, y_test) * 100}%.")
    genauigkeitswerte.append((i, accuracy_score(predictions, y_test) * 100))
hoechster_genauigkeitswert = max(genauigkeitswerte, key=lambda x: x[1])
printf(
    f"Der höchste Genauigkeitswert der erreicht wurde liegt bei {hoechster_genauigkeitswert[1]}%, bei der betrachtung von {hoechster_genauigkeitswert[0]} Nachbarn.")
