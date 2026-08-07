import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

for rs in [0,10,42]:

    X_train, X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.3,random_state=rs
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    print("Random State =",rs)
    print("Accuracy =",accuracy_score(y_test,pred))
    print()