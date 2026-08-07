import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("Feature Importance\n")

for name, score in zip(X.columns, model.feature_importances_):
    print(f"{name} : {score:.4f}")

most = X.columns[model.feature_importances_.argmax()]
least = X.columns[model.feature_importances_.argmin()]

print("\nMost Important Feature :", most)
print("Least Important Feature:", least)