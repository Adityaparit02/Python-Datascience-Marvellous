import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,random_state=42
)

model = DecisionTreeClassifier(
    max_depth=None,
    random_state=42
)

model.fit(X_train,y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Training Accuracy :",accuracy_score(y_train,train_pred))
print("Testing Accuracy  :",accuracy_score(y_test,test_pred))
print("\nIf training accuracy is 100% but testing accuracy is lower, the model is overfitting.")