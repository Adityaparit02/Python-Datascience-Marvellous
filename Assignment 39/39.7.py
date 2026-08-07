"""
Q7. Use the trained model to predict result for a student with:
- StudyHours = 6
- Attendance = 85
- PreviousScore = 66
- AssignmentsCompleted = 7
- SleepHours = 7
Will the student Pass or Fail?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

X = df[['StudyHours', 'Attendance', 'PreviousScore',
        'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# New student data
new_student = pd.DataFrame({
    'StudyHours': [6],
    'Attendance': [85],
    'PreviousScore': [66],
    'AssignmentsCompleted': [7],
    'SleepHours': [7]
})

# Predict
prediction = model.predict(new_student)

result = "PASS" if prediction[0] == 1 else "FAIL"
print("----- Prediction for new student -----")
print(new_student)
print(f"\nPredicted FinalResult: {prediction[0]} --> The student will {result}.")