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

new_students = pd.DataFrame({
    "StudyHours":[2,5,7,8,4],
    "Attendance":[70,85,90,95,78],
    "PreviousScore":[60,72,85,91,68],
    "AssignmentsCompleted":[4,7,9,10,5],
    "SleepHours":[6,7,8,7,6]
})

prediction = model.predict(new_students)

new_students["Prediction"] = prediction
new_students["Prediction"] = new_students["Prediction"].map({1:"Pass",0:"Fail"})

print(new_students)