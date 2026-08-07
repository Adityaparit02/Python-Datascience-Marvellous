import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("student_performance_ml.csv")

# Original Accuracy
X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

old_acc = accuracy_score(y_test, model.predict(X_test))

# Remove SleepHours
X = df.drop(["SleepHours", "FinalResult"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

new_acc = accuracy_score(y_test, model.predict(X_test))

print("Original Accuracy :", old_acc)
print("New Accuracy      :", new_acc)