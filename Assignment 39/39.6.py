"""
Q6. Train three Decision Tree models with:
- max_depth = 1
- max_depth = 3
- max_depth = None
Compare their testing accuracies and write your observations.
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

# Dictionary to store results
depths = [1, 3, None]
results = {}

for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[depth] = acc
    print(f"max_depth = {depth} --> Testing Accuracy = {acc * 100:.2f}%")

print("\n----- Summary -----")
for depth, acc in results.items():
    print(f"max_depth = {depth}: {acc * 100:.2f}%")

print("""
Observations:
1. max_depth = 1 (very shallow tree): The model is too simple and likely
   underfits the data, resulting in lower accuracy since it can only make
   one split/decision.
2. max_depth = 3 (moderate depth): The model captures more patterns and
   usually gives a balanced, good accuracy without being too complex.
3. max_depth = None (fully grown tree): The tree keeps splitting until
   all leaves are pure, which can lead to overfitting - high accuracy on
   training data but not necessarily the best on testing data.
4. Overall, increasing max_depth improves accuracy up to a point, after
   which the model starts to overfit the training data.
""")