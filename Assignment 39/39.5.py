"""
Q5. Calculate:
- Training accuracy
- Testing accuracy
Compare both and comment whether the model is overfitting or underfitting.
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

# Predictions on training and testing data
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate accuracies
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("----- Training Accuracy -----")
print(f"{train_accuracy * 100:.2f}%")

print("\n----- Testing Accuracy -----")
print(f"{test_accuracy * 100:.2f}%")

# Compare and comment
diff = train_accuracy - test_accuracy
print(f"\nDifference (Train - Test): {diff * 100:.2f}%")

if train_accuracy >= 0.95 and diff > 0.15:
    print("\nComment: The model is OVERFITTING - it performs very well on "
          "training data but significantly worse on testing data. This "
          "means the model has memorized the training data instead of "
          "learning general patterns.")
elif train_accuracy < 0.70 and test_accuracy < 0.70:
    print("\nComment: The model is UNDERFITTING - both training and "
          "testing accuracy are low, meaning the model is too simple to "
          "capture the underlying patterns in the data.")
else:
    print("\nComment: The model shows a GOOD FIT - training and testing "
          "accuracies are close to each other, meaning the model "
          "generalizes reasonably well to unseen data.")