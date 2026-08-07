"""
Q8. Write a single structured Python program that performs:
1. Dataset loading
2. Data analysis
3. Visualization
4. Train-test split
5. Model training
6. Prediction
7. Accuracy calculation
8. Confusion matrix generation
9. Final conclusion
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ------------------------------------------------------------
# Step 1: Dataset Loading
# ------------------------------------------------------------
df = pd.read_csv("student_performance_ml.csv")
print("----- Dataset Loaded -----")
print(df.head())

# ------------------------------------------------------------
# Step 2: Data Analysis
# ------------------------------------------------------------
print("\n----- Dataset Shape -----")
print(df.shape)

print("\n----- Data types -----")
print(df.dtypes)

print("\n----- FinalResult distribution -----")
print(df['FinalResult'].value_counts())

print("\n----- Summary statistics -----")
print(df.describe())

# ------------------------------------------------------------
# Step 3: Visualization
# ------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df['StudyHours'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("DT_Q8_studyhours_histogram.png")
plt.show()

# ------------------------------------------------------------
# Step 4: Train-Test Split
# ------------------------------------------------------------
X = df[['StudyHours', 'Attendance', 'PreviousScore',
        'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {len(X_train)}, Testing samples: {len(X_test)}")

# ------------------------------------------------------------
# Step 5: Model Training
# ------------------------------------------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("\nModel training completed.")

# ------------------------------------------------------------
# Step 6: Prediction
# ------------------------------------------------------------
y_pred = model.predict(X_test)
results_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print("\n----- Predicted vs Actual -----")
print(results_df)

# ------------------------------------------------------------
# Step 7: Accuracy Calculation
# ------------------------------------------------------------
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# ------------------------------------------------------------
# Step 8: Confusion Matrix Generation
# ------------------------------------------------------------
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Fail (0)', 'Pass (1)'])
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("DT_Q8_confusion_matrix.png")
plt.show()

# ------------------------------------------------------------
# Step 9: Final Conclusion
# ------------------------------------------------------------
print(f"""
----- Final Conclusion -----
The Decision Tree Classifier achieved a testing accuracy of
{accuracy * 100:.2f}% in predicting whether a student will Pass or Fail.
Based on the confusion matrix, we can see how many predictions were
correct (True Positives/Negatives) versus incorrect (False
Positives/Negatives). This model can be used as a baseline to help
identify students who may need additional academic support, though
further tuning (e.g., adjusting max_depth) could improve generalization.
""")