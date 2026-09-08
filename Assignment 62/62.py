import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score,confusion_matrix

import matplotlib.pyplot as plt

border = "#"*120
borderx = "-"*70

######################################################################
#       Load Dataset
######################################################################
Data = pd.read_csv("Employee_Attrition.csv")

######################################################################
#      Display shape columns and first five records
######################################################################
print()
print()
print(border)

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


######################################################################
#      Check for missing values
######################################################################
print()
print()
print(border)

print(borderx)
print("Null values in the Dataset : ")
print(borderx)
print(Data.isnull().sum())
print(borderx)



######################################################################
#      Check for categorical and numeric values  
######################################################################
print()
print()
print(border)

print(borderx)
print("Info of Categorical and Numeric Data :  ")
print(borderx)
print(Data.info())
print(borderx)

######################################################################
#      Convert categorical data in Numeric  
######################################################################
print()
print()
print(border)

Data = pd.get_dummies(Data,columns=["OverTime"] ,dtype=int)

print(borderx)
print("Encoded Categorical Value Datsset :")
print(borderx)

print(Data.head())
print(borderx)

######################################################################
#      Convert Target Column in binary   
######################################################################
print()
print()
print(border)

Data["Attrition"] = Data["Attrition"].map({"Yes" : 1 , "No" : 0})
print(borderx)
print("Encoded Attrition Column to Binary : ")
print(borderx)
print(Data.head())
print(borderx)

######################################################################
#      Seperate Independent and Dependent Variables   
######################################################################
print()
print()
print(border)
print(borderx)
print("Seperated Independat and Dependant Variables : ")
print(borderx)

FEATURE_COLUMNS = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears',
                    'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance',
                    'OverTime_No', 'OverTime_Yes',
                    'NumCompaniesWorked', 'TrainingTimesLastYear']

X = Data[FEATURE_COLUMNS]

Y = Data["Attrition"]

######################################################################
#      Seperate Train and Test Data   
######################################################################
print()
print()
print(border)
print(borderx)
print("Seperated Train and Test Data : ")
print(borderx)

X_Train , X_Test , Y_Train , Y_Test = train_test_split(X,Y , test_size=0.3 , random_state=42 , stratify=Y)

######################################################################
#      Scale the Data   
######################################################################
print()
print()
print(border)
print(borderx)
print("Scaled the Data: ")
print(borderx)
Scaler = StandardScaler()

X_Train = Scaler.fit_transform(X_Train)
X_Test = Scaler.transform(X_Test)


######################################################################
#      Create a MLP Model   
######################################################################
print()
print()
print(border)
print(borderx)
print("Create a MLP Model : ")
print(borderx)
Model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation='relu',
    solver='adam',
    max_iter=2000,
    random_state=42
)

######################################################################
#      Train the MLP Model   
######################################################################
print()
print()
print(border)
print(borderx)
print("Train the MLP Model : ")
print(borderx)
Model = Model.fit(X_Train,Y_Train)

######################################################################
#      Number of Iterations required to Train the Model  
######################################################################
print()
print()
print(border)
print(borderx)
print("Number of Iterations required to Train the Model : ")
print()

print(borderx)
print("Number of Iterations required to train the Model : ",Model.n_iter_,"iterations")
print(borderx)



######################################################################
#      Test the MLP Model   
######################################################################
print()
print()
print(border)
print(borderx)
print("Test the MLP Model : ")

Y_Train_Pred = Model.predict(X_Train)
Y_Test_Pred = Model.predict(X_Test)

train_accuracy = accuracy_score(Y_Train,Y_Train_Pred)
test_accuracy = accuracy_score(Y_Test,Y_Test_Pred)

print(borderx)
print("Training accuracy of Model : ",train_accuracy*100)
print(borderx)
print("Testing accuracy of Model : ",test_accuracy*100)
print(borderx)


######################################################################
#      Confusion Matrix generation   
######################################################################
print()
print()
print(border)
print(borderx)
print("Confusion Matrix generation : ")
print(borderx)
print(confusion_matrix(Y_Test,Y_Test_Pred))
print(borderx)


######################################################################
#      Plot the Loss Curve   
######################################################################
print()
print()
print(border)
print(borderx)
print("Plot the Loss Curve : ")

plt.plot(Model.loss_curve_)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")

plt.savefig("loss_curve.png")
plt.show()


######################################################################
#      Task 17: PredictAttrition function
######################################################################
print()
print()
print(border)
print(borderx)
print("Defining PredictAttrition Function : ")
print(borderx)

def PredictAttrition(employee_data):
    """
    Predicts employee attrition for one or more employees.

    Parameters
    ----------
    employee_data : dict or list of dicts
        Each dict must contain the following keys:
        'Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears',
        'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance',
        'OverTime' ("Yes" or "No"),
        'NumCompaniesWorked', 'TrainingTimesLastYear'

    Returns
    -------
    pandas.DataFrame
        Original input fields plus the predicted label ('Yes'/'No')
        and the predicted probability of attrition.
    """
    # Allow a single dict or a list of dicts
    if isinstance(employee_data, dict):
        employee_data = [employee_data]

    InputDf = pd.DataFrame(employee_data)

    # One-hot encode OverTime the same way as training data
    InputDf["OverTime_No"] = (InputDf["OverTime"] == "No").astype(int)
    InputDf["OverTime_Yes"] = (InputDf["OverTime"] == "Yes").astype(int)

    # Ensure column order matches training features exactly
    InputFeatures = InputDf[FEATURE_COLUMNS]

    # Scale using the SAME scaler fitted on training data
    ScaledInput = Scaler.transform(InputFeatures)

    Predictions = Model.predict(ScaledInput)
    Probabilities = Model.predict_proba(ScaledInput)[:, 1]

    ResultDf = InputDf.copy()
    ResultDf["Predicted_Attrition"] = pd.Series(Predictions).map({1: "Yes", 0: "No"})
    ResultDf["Attrition_Probability"] = Probabilities.round(3)

    return ResultDf


######################################################################
#      Task 18: Test the system using new employee records
######################################################################
print()
print()
print(border)
print(borderx)
print("Testing PredictAttrition on New Employee Records : ")
print(borderx)

NewEmployees = [
    {"Age": 29, "MonthlyIncome": 3200, "YearsAtCompany": 1, "TotalWorkingYears": 2,
     "DistanceFromHome": 15, "JobSatisfaction": 2, "WorkLifeBalance": 1,
     "OverTime": "Yes", "NumCompaniesWorked": 3, "TrainingTimesLastYear": 1},

    {"Age": 45, "MonthlyIncome": 9800, "YearsAtCompany": 15, "TotalWorkingYears": 20,
     "DistanceFromHome": 3, "JobSatisfaction": 4, "WorkLifeBalance": 3,
     "OverTime": "No", "NumCompaniesWorked": 1, "TrainingTimesLastYear": 3},

    {"Age": 34, "MonthlyIncome": 5400, "YearsAtCompany": 5, "TotalWorkingYears": 8,
     "DistanceFromHome": 8, "JobSatisfaction": 3, "WorkLifeBalance": 2,
     "OverTime": "No", "NumCompaniesWorked": 2, "TrainingTimesLastYear": 2},

    {"Age": 24, "MonthlyIncome": 2600, "YearsAtCompany": 1, "TotalWorkingYears": 1,
     "DistanceFromHome": 22, "JobSatisfaction": 1, "WorkLifeBalance": 1,
     "OverTime": "Yes", "NumCompaniesWorked": 4, "TrainingTimesLastYear": 0},

    {"Age": 52, "MonthlyIncome": 12000, "YearsAtCompany": 25, "TotalWorkingYears": 30,
     "DistanceFromHome": 5, "JobSatisfaction": 4, "WorkLifeBalance": 4,
     "OverTime": "No", "NumCompaniesWorked": 1, "TrainingTimesLastYear": 4},
]

PredictionResults = PredictAttrition(NewEmployees)
print(PredictionResults)
print(borderx)


######################################################################
#      Task 19: Overfitting / Underfitting Analysis
######################################################################
print()
print()
print(border)
print(borderx)
print("Overfitting / Underfitting Analysis : ")
print(borderx)

accuracy_gap = (train_accuracy - test_accuracy) * 100

print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
print("Testing  Accuracy : {:.2f}%".format(test_accuracy * 100))
print("Gap (Train - Test): {:.2f}%".format(accuracy_gap))
print(borderx)

if train_accuracy < 0.75 and test_accuracy < 0.75:
    Verdict = ("The model shows UNDERFITTING: both training and testing "
               "accuracy are low, meaning the network has not learned the "
               "underlying patterns well enough.")
elif accuracy_gap > 10:
    Verdict = ("The model shows OVERFITTING: training accuracy is "
               "considerably higher than testing accuracy, meaning it has "
               "memorized the training data rather than generalizing.")
else:
    Verdict = ("The model appears to be a GOOD FIT: training and testing "
               "accuracies are close together and both are reasonably high, "
               "indicating the network generalizes well to unseen data.")

print(Verdict)
print(borderx)