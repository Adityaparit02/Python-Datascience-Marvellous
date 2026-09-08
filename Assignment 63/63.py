import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, confusion_matrix,
                              classification_report, precision_score,
                              recall_score, f1_score)

import matplotlib.pyplot as plt

border = "#"*120
borderx = "-"*70

######################################################################
# Task 1: Load and understand the dataset
######################################################################
print()
print()
print(border)
print(borderx)
print("Loading the Dataset : ")
print(borderx)

Data = pd.read_csv("Loan_Default.csv")

print(borderx)
print("Shape of Dataset :")
print(borderx)
print(Data.shape)
print(borderx)

print(borderx)
print("Columns of Dataset :")
print(borderx)
print(Data.columns)
print(borderx)

print(borderx)
print("First five Records in Dataset :")
print(borderx)
print(Data.head())
print(borderx)

print(borderx)
print("Data Types :")
print(borderx)
print(Data.dtypes)
print(borderx)


######################################################################
# Task 2: Perform exploratory analysis
######################################################################
print()
print()
print(border)
print(borderx)
print("Exploratory Analysis : ")
print(borderx)

print(borderx)
print("Statistical Summary of Numeric Columns : ")
print(borderx)
print(Data.describe())
print(borderx)

print(borderx)
print("Unique Values in Categorical Columns : ")
print(borderx)
for col in Data.select_dtypes(include="object").columns:
    print(col, ":", Data[col].unique())
print(borderx)


######################################################################
# Task 3: Find missing values
######################################################################
print()
print()
print(border)
print(borderx)
print("Missing Values in the Dataset : ")
print(borderx)
print(Data.isnull().sum())
print(borderx)


######################################################################
# Task 4: Check whether the target classes are balanced
######################################################################
print()
print()
print(border)
print(borderx)
print("Target Class Balance ('Default') : ")
print(borderx)

class_counts = Data["Default"].value_counts()
class_pct = Data["Default"].value_counts(normalize=True) * 100

print(class_counts)
print(borderx)
print(class_pct.round(2).astype(str) + " %")
print(borderx)

plt.figure()
class_counts.plot(kind="bar", color=["steelblue", "indianred"])
plt.xlabel("Default")
plt.ylabel("Count")
plt.title("Target Class Distribution")
plt.xticks(rotation=0)
plt.savefig("class_balance.png")
plt.close()

print(borderx)
if class_pct.min() < 30:
    print("The target classes are IMBALANCED. Stratified splitting and/or "
          "class-weighting should be considered.")
else:
    print("The target classes are reasonably BALANCED.")
print(borderx)


######################################################################
# Task 5: Encode categorical variables
######################################################################
print()
print()
print(border)
print(borderx)
print("Encoding Categorical Variables : ")
print(borderx)

# Keep the original HomeOwnership categories for later use by PredictDefault()
HOMEOWNERSHIP_CATEGORIES = sorted(Data["HomeOwnership"].dropna().unique().tolist())

Data = pd.get_dummies(Data, columns=["HomeOwnership"], dtype=int)
HOMEOWNERSHIP_DUMMY_COLUMNS = [c for c in Data.columns if c.startswith("HomeOwnership_")]

Data["PreviousDefault"] = Data["PreviousDefault"].map({"Yes": 1, "No": 0})

print(borderx)
print("Encoded Dataset (first 5 rows) : ")
print(borderx)
print(Data.head())
print(borderx)


######################################################################
# Task 6: Separate X and y
######################################################################
print()
print()
print(border)
print(borderx)
print("Separating X and y : ")
print(borderx)

FEATURE_COLUMNS = ['Age', 'Income', 'LoanAmount', 'CreditScore', 'EmploymentYears',
                    'ExistingLoans', 'MonthlyDebt', 'LoanTerm',
                    'PreviousDefault'] + HOMEOWNERSHIP_DUMMY_COLUMNS

X = Data[FEATURE_COLUMNS]
Y = Data["Default"]

print(borderx)
print("X shape :", X.shape, " | Y shape :", Y.shape)
print(borderx)


######################################################################
# Task 7: Split the dataset into training and testing data
######################################################################
print()
print()
print(border)
print(borderx)
print("Splitting Train/Test Data : ")
print(borderx)

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
    X, Y, test_size=0.3, random_state=42, stratify=Y
)

print(borderx)
print("X_Train :", X_Train.shape, " | X_Test :", X_Test.shape)
print(borderx)


######################################################################
# Task 8: Explain whether stratified splitting should be used
######################################################################
print()
print()
print(border)
print(borderx)
print("Stratified Splitting - Explanation : ")
print(borderx)
print(
    "Stratified splitting (stratify=Y) preserves the same proportion of "
    "'Default' vs 'Non-Default' cases in both the training and testing "
    "sets as in the full dataset. This matters most when the target "
    "classes are imbalanced (as checked in Task 4) - without it, a "
    "random split could under-represent the minority class in the test "
    "set, giving a misleading picture of model performance. Since loan "
    "default is typically a minority-class problem, stratified splitting "
    "is used here (see the train_test_split call above)."
)
print(borderx)


######################################################################
# Task 9: Scale the features
######################################################################
print()
print()
print(border)
print(borderx)
print("Scaling Features : ")
print(borderx)

Scaler = StandardScaler()
X_Train_Scaled = Scaler.fit_transform(X_Train)
X_Test_Scaled = Scaler.transform(X_Test)


######################################################################
# Task 10: Create an MLPClassifier
######################################################################
print()
print()
print(border)
print(borderx)
print("Creating MLPClassifier : ")
print(borderx)

Model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)


######################################################################
# Task 11: Train the model
######################################################################
print()
print()
print(border)
print(borderx)
print("Training the Model : ")
print(borderx)

Model = Model.fit(X_Train_Scaled, Y_Train)

print(borderx)
print("Iterations to converge :", Model.n_iter_)
print(borderx)


######################################################################
# Task 12: Calculate accuracy
######################################################################
print()
print()
print(border)
print(borderx)
print("Calculating Accuracy : ")
print(borderx)

Y_Train_Pred = Model.predict(X_Train_Scaled)
Y_Test_Pred = Model.predict(X_Test_Scaled)

train_accuracy = accuracy_score(Y_Train, Y_Train_Pred)
test_accuracy = accuracy_score(Y_Test, Y_Test_Pred)

print(borderx)
print("Training Accuracy :", round(train_accuracy * 100, 2), "%")
print("Testing  Accuracy :", round(test_accuracy * 100, 2), "%")
print(borderx)


######################################################################
# Task 13: Generate the confusion matrix
######################################################################
print()
print()
print(border)
print(borderx)
print("Confusion Matrix : ")
print(borderx)

cm = confusion_matrix(Y_Test, Y_Test_Pred)
print(cm)
print(borderx)


######################################################################
# Task 14: Generate the classification report
######################################################################
print()
print()
print(border)
print(borderx)
print("Classification Report : ")
print(borderx)

print(classification_report(Y_Test, Y_Test_Pred))
print(borderx)


######################################################################
# Task 15: Calculate precision, recall and F1-score
######################################################################
print()
print()
print(border)
print(borderx)
print("Precision, Recall, F1-score (positive class = Default) : ")
print(borderx)

precision = precision_score(Y_Test, Y_Test_Pred)
recall = recall_score(Y_Test, Y_Test_Pred)
f1 = f1_score(Y_Test, Y_Test_Pred)

print("Precision :", round(precision, 4))
print("Recall    :", round(recall, 4))
print("F1-score  :", round(f1, 4))
print(borderx)


######################################################################
# Task 16: Plot training loss
######################################################################
print()
print()
print(border)
print(borderx)
print("Plotting Training Loss : ")
print(borderx)

plt.figure()
plt.plot(Model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.savefig("loss_curve.png")
plt.close()


######################################################################
# Task 17: Test the model on new loan applicants
######################################################################
print()
print()
print(border)
print(borderx)
print("Testing on New Loan Applicants : ")
print(borderx)

def PredictDefault(loan_data, model, scaler):
    """
    Predicts loan default for one or more applicants using a given
    fitted model and scaler.

    Parameters
    ----------
    loan_data : dict or list of dicts
        Keys: 'Age', 'Income', 'LoanAmount', 'CreditScore',
        'EmploymentYears', 'ExistingLoans', 'MonthlyDebt', 'LoanTerm',
        'PreviousDefault' ("Yes"/"No"), 'HomeOwnership'
    model : fitted classifier with .predict / .predict_proba
    scaler : fitted StandardScaler

    Returns
    -------
    pandas.DataFrame with predicted label and probability appended.
    """
    if isinstance(loan_data, dict):
        loan_data = [loan_data]

    InputDf = pd.DataFrame(loan_data)
    InputDf["PreviousDefault"] = InputDf["PreviousDefault"].map({"Yes": 1, "No": 0})

    for col in HOMEOWNERSHIP_DUMMY_COLUMNS:
        category = col.replace("HomeOwnership_", "")
        InputDf[col] = (InputDf["HomeOwnership"] == category).astype(int)

    InputFeatures = InputDf[FEATURE_COLUMNS]
    ScaledInput = scaler.transform(InputFeatures)

    Predictions = model.predict(ScaledInput)
    Probabilities = model.predict_proba(ScaledInput)[:, 1]

    ResultDf = InputDf.copy()
    ResultDf["Predicted_Default"] = pd.Series(Predictions).map({1: "Yes", 0: "No"})
    ResultDf["Default_Probability"] = Probabilities.round(3)
    return ResultDf


# NOTE: adjust HomeOwnership values to match HOMEOWNERSHIP_CATEGORIES if needed
NewApplicants = [
    {"Age": 25, "Income": 28000, "LoanAmount": 15000, "CreditScore": 580,
     "EmploymentYears": 1, "ExistingLoans": 2, "MonthlyDebt": 900,
     "LoanTerm": 36, "PreviousDefault": "Yes", "HomeOwnership": "Rent"},

    {"Age": 42, "Income": 95000, "LoanAmount": 20000, "CreditScore": 780,
     "EmploymentYears": 15, "ExistingLoans": 0, "MonthlyDebt": 300,
     "LoanTerm": 24, "PreviousDefault": "No", "HomeOwnership": "Own"},

    {"Age": 34, "Income": 55000, "LoanAmount": 30000, "CreditScore": 690,
     "EmploymentYears": 8, "ExistingLoans": 1, "MonthlyDebt": 700,
     "LoanTerm": 48, "PreviousDefault": "No", "HomeOwnership": "Mortgage"},

    {"Age": 29, "Income": 32000, "LoanAmount": 25000, "CreditScore": 610,
     "EmploymentYears": 2, "ExistingLoans": 3, "MonthlyDebt": 1100,
     "LoanTerm": 60, "PreviousDefault": "Yes", "HomeOwnership": "Rent"},

    {"Age": 50, "Income": 120000, "LoanAmount": 10000, "CreditScore": 810,
     "EmploymentYears": 22, "ExistingLoans": 0, "MonthlyDebt": 200,
     "LoanTerm": 12, "PreviousDefault": "No", "HomeOwnership": "Own"},
]

NewPredictions = PredictDefault(NewApplicants, Model, Scaler)
print(NewPredictions)
print(borderx)


######################################################################
# HYPERPARAMETER EXPERIMENTS
# Each experiment changes ONE parameter at a time, keeping all others
# fixed at the Task 10 baseline (hidden_layer_sizes=(32,16),
# activation='relu', solver='adam', max_iter=1000, random_state=42).
######################################################################

def evaluate_model(model):
    """Fit a model on the training data and return train/test accuracy."""
    model.fit(X_Train_Scaled, Y_Train)
    tr_acc = accuracy_score(Y_Train, model.predict(X_Train_Scaled))
    te_acc = accuracy_score(Y_Test, model.predict(X_Test_Scaled))
    return model, tr_acc, te_acc


######################################################################
# Experiment 1: Activation Function
######################################################################
print()
print()
print(border)
print(borderx)
print("Experiment 1 - Activation Function : ")
print(borderx)

activations = ["identity", "logistic", "tanh", "relu"]
activation_results = []

for act in activations:
    m = MLPClassifier(hidden_layer_sizes=(32, 16), activation=act,
                       solver='adam', max_iter=1000, random_state=42)
    _, tr_acc, te_acc = evaluate_model(m)
    activation_results.append((act, tr_acc, te_acc))
    print(f"Activation = {act:10s} | Train Acc = {tr_acc*100:6.2f}% | Test Acc = {te_acc*100:6.2f}%")

print(borderx)

plt.figure()
labels = [r[0] for r in activation_results]
train_vals = [r[1]*100 for r in activation_results]
test_vals = [r[2]*100 for r in activation_results]
x_pos = np.arange(len(labels))
plt.bar(x_pos - 0.2, train_vals, width=0.4, label="Train Accuracy")
plt.bar(x_pos + 0.2, test_vals, width=0.4, label="Test Accuracy")
plt.xticks(x_pos, labels)
plt.ylabel("Accuracy (%)")
plt.title("Experiment 1: Accuracy vs Activation Function")
plt.legend()
plt.savefig("experiment1_activation.png")
plt.close()


######################################################################
# Experiment 2: Hidden Layer Sizes
######################################################################
print()
print()
print(border)
print(borderx)
print("Experiment 2 - Hidden Layer Sizes : ")
print(borderx)

hidden_layer_options = [(10,), (20, 10), (50, 25), (100, 50, 25)]
hidden_layer_results = []

for hls in hidden_layer_options:
    m = MLPClassifier(hidden_layer_sizes=hls, activation='relu',
                       solver='adam', max_iter=1000, random_state=42)
    _, tr_acc, te_acc = evaluate_model(m)
    hidden_layer_results.append((str(hls), tr_acc, te_acc))
    print(f"Hidden Layers = {str(hls):15s} | Train Acc = {tr_acc*100:6.2f}% | Test Acc = {te_acc*100:6.2f}%")

print(borderx)

plt.figure()
labels = [r[0] for r in hidden_layer_results]
train_vals = [r[1]*100 for r in hidden_layer_results]
test_vals = [r[2]*100 for r in hidden_layer_results]
x_pos = np.arange(len(labels))
plt.bar(x_pos - 0.2, train_vals, width=0.4, label="Train Accuracy")
plt.bar(x_pos + 0.2, test_vals, width=0.4, label="Test Accuracy")
plt.xticks(x_pos, labels)
plt.ylabel("Accuracy (%)")
plt.title("Experiment 2: Accuracy vs Hidden Layer Sizes")
plt.legend()
plt.savefig("experiment2_hidden_layers.png")
plt.close()


######################################################################
# Experiment 3: Learning Rate (learning_rate_init)
######################################################################
print()
print()
print(border)
print(borderx)
print("Experiment 3 - Learning Rate (learning_rate_init) : ")
print(borderx)

learning_rates = [0.0001, 0.001, 0.01, 0.1]
lr_results = []

for lr in learning_rates:
    m = MLPClassifier(hidden_layer_sizes=(32, 16), activation='relu',
                       solver='adam', learning_rate_init=lr,
                       max_iter=1000, random_state=42)
    _, tr_acc, te_acc = evaluate_model(m)
    lr_results.append((lr, tr_acc, te_acc))
    print(f"learning_rate_init = {lr:<8} | Train Acc = {tr_acc*100:6.2f}% | Test Acc = {te_acc*100:6.2f}%")

print(borderx)

plt.figure()
labels = [str(r[0]) for r in lr_results]
train_vals = [r[1]*100 for r in lr_results]
test_vals = [r[2]*100 for r in lr_results]
x_pos = np.arange(len(labels))
plt.bar(x_pos - 0.2, train_vals, width=0.4, label="Train Accuracy")
plt.bar(x_pos + 0.2, test_vals, width=0.4, label="Test Accuracy")
plt.xticks(x_pos, labels)
plt.ylabel("Accuracy (%)")
plt.title("Experiment 3: Accuracy vs Learning Rate Init")
plt.legend()
plt.savefig("experiment3_learning_rate.png")
plt.close()


######################################################################
# Summary of all experiments
######################################################################
print()
print()
print(border)
print(borderx)
print("Hyperparameter Experiment Summary : ")
print(borderx)
print("Best activation (by test acc)      :", max(activation_results, key=lambda r: r[2])[0])
print("Best hidden layer config (test acc):", max(hidden_layer_results, key=lambda r: r[2])[0])
print("Best learning_rate_init (test acc) :", max(lr_results, key=lambda r: r[2])[0])
print(borderx)