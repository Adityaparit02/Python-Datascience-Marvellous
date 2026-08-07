"""
Q4. Generate confusion matrix using sklearn.
Display it using ConfusionMatrixDisplay.
Explain clearly: True Positive, True Negative, False Positive, False Negative.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("----- Confusion Matrix -----")
print(cm)

# Display confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Fail (0)', 'Pass (1)'])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("DT_Q4_confusion_matrix.png")
plt.show()

# Extract TP, TN, FP, FN (for binary classification: 0=Fail, 1=Pass)
tn, fp, fn, tp = cm.ravel()

print(f"\nTrue Positive (TP)  = {tp}")
print(f"True Negative (TN)  = {tn}")
print(f"False Positive (FP) = {fp}")
print(f"False Negative (FN) = {fn}")

print("""
Explanation:
- True Positive (TP): Student actually PASSED and the model correctly
  predicted PASS.
- True Negative (TN): Student actually FAILED and the model correctly
  predicted FAIL.
- False Positive (FP): Student actually FAILED but the model incorrectly
  predicted PASS (Type I error).
- False Negative (FN): Student actually PASSED but the model incorrectly
  predicted FAIL (Type II error).
""")