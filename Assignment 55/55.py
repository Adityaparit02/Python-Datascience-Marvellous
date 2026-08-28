import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score

border = "-"*70
##################################################
#                Data Loading                   #
##################################################
df = pd.read_csv("Customer_Loan_Approval.csv")

##################################################
#                Data Checking                  #
##################################################
print(border)
print("Null Values Found : ")
print(df.isnull().sum())
print(border)


##################################################
#                Data Splitting                 #
##################################################
X = df.drop(columns=["LoanApproved"])
Y = df["LoanApproved"]

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


##################################################
#              Logistic Regression              #
##################################################
LogisticReg_Model = LogisticRegression()
LogisticReg_Model = LogisticReg_Model.fit(X_train,Y_train)

Y_Pred = LogisticReg_Model.predict(X_test)

Logistic_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)
print("Accuracy of Logistic Regression is : ",Logistic_Accuracy*100)
print(border)

Accuracy = 0
Y_Pred = 0

##################################################
#               Decision Tree                  #
##################################################
DecisionTree_Model = DecisionTreeClassifier()
DecisionTree_Model = DecisionTree_Model.fit(X_train,Y_train)

Y_Pred = DecisionTree_Model.predict(X_test)

DecisionTree_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)
print("Accuracy of Decision Tree Classfier is : ", DecisionTree_Accuracy*100)
print(border)

Accuracy = 0
Y_Pred = 0


##################################################
#                    KNN                       #
##################################################
KNN_Model = KNeighborsClassifier(n_neighbors=5)
KNN_Model = KNN_Model.fit(X_train,Y_train)

Y_Pred = KNN_Model.predict(X_test)

KNN_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)
print("Accuracy of KNN Classifier is : ", KNN_Accuracy*100)
print(border)


##################################################
#             Creating Hard Voting Model         #
##################################################
Model = VotingClassifier(estimators=[
    ('logistic',LogisticReg_Model),
    ('decision_tree',DecisionTree_Model),
    ('knn',KNN_Model)
]   ,voting="hard")


Model = Model.fit(X_train,Y_train)

Y_Pred = Model.predict(X_test)

HardVoting_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)
print("Accuracy of Hard Voting Model : ",HardVoting_Accuracy*100)
print(border)


##################################################
#       Creating Soft Voting Model              #
##################################################
Model = VotingClassifier(estimators=[
    ('logistic',LogisticReg_Model),
    ('decision_tree',DecisionTree_Model),
    ('knn',KNN_Model)
]   ,voting="soft")


Model = Model.fit(X_train,Y_train)

Y_Pred = Model.predict(X_test)

SoftVoting_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)
print("Accuracy of Soft Voting Model : ",SoftVoting_Accuracy*100)
print(border)
print(border)

##################################################
#              Model Accuracy Table              #
##################################################

Accuracy_Table = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],
    "Accuracy": [
        Logistic_Accuracy * 100,
        DecisionTree_Accuracy * 100,
        KNN_Accuracy * 100,
        HardVoting_Accuracy * 100,
        SoftVoting_Accuracy * 100
    ]
})

print("\n")
print(border)
print("                  MODEL ACCURACY")
print(border)
print(Accuracy_Table.to_string(index=False))
print(border)
print("\n")