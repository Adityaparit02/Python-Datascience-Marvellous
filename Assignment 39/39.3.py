"""
Q3. Calculate model accuracy using accuracy_score.
Display the result in percentage format.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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

# Predict
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("----- Model Accuracy -----")
print(f"Accuracy: {accuracy * 100:.2f}%")