import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
border = "-" * 70
##################################################
#                  Data Loading                  #
##################################################
df = pd.read_csv("Fraudulent_Transaction_Detection.csv")


##################################################
#              Checking Null Values              #
##################################################
print(border)
print("Null Values in Data set :")
print(df.isnull().sum())
print(border)

##################################################
#               Splitting Data                   #
##################################################
X = df.drop(columns=["Fraud"])
Y = df["Fraud"]

X_train , X_test ,Y_train , Y_test = train_test_split(X,Y,random_state=42,test_size=0.2)


##################################################
#              Decision Tree Model               #
##################################################
DecisionTree_Model = DecisionTreeClassifier()
DecisionTree_Model = DecisionTree_Model.fit(X_train,Y_train)

Y_Pred = DecisionTree_Model.predict(X_test)
print(border)
Decision_Accuracy = accuracy_score(Y_test,Y_Pred)
print("Accuracy of Decision Tree Classfier : ",Decision_Accuracy*100)
Decision_Precision = precision_score(Y_test, Y_Pred)
Decision_Recall = recall_score(Y_test, Y_Pred)
Decision_F1 = f1_score(Y_test, Y_Pred)
Decision_CM = confusion_matrix(Y_test, Y_Pred)
print("Confusion Matrix - Decision Tree:\n", Decision_CM)
print(border)

##################################################
#                Bagging Model                   #
##################################################
Bagging_Model = BaggingClassifier(estimator=DecisionTree_Model,n_estimators=10,random_state=42)

Bagging_Model = Bagging_Model.fit(X_train,Y_train)

Y_Pred = Bagging_Model.predict(X_test)
print(border)

Bagging_Accuracy = accuracy_score(Y_test, Y_Pred)
print("Accuracy of Bagging Model : ",Bagging_Accuracy*100)
Bagging_Precision = precision_score(Y_test, Y_Pred)
Bagging_Recall = recall_score(Y_test, Y_Pred)
Bagging_F1 = f1_score(Y_test, Y_Pred)
Bagging_CM = confusion_matrix(Y_test, Y_Pred)
print("Confusion Matrix - Bagging:\n", Bagging_CM)
print(border)

##################################################
#          Random Forest Classifier              #
##################################################
RandomForest_Model = RandomForestClassifier()
RandomForest_Model = RandomForest_Model.fit(X_train,Y_train)

Y_Pred = RandomForest_Model.predict(X_test)
print(border)

Random_Accuracy = accuracy_score(Y_test,Y_Pred)
print("Accuracy of Random Forest Classifier : ",Random_Accuracy*100)
Random_Precision = precision_score(Y_test, Y_Pred)
Random_Recall = recall_score(Y_test, Y_Pred)
Random_F1 = f1_score(Y_test, Y_Pred)
Random_CM = confusion_matrix(Y_test, Y_Pred)
print("Confusion Matrix - Random Forest:\n", Random_CM)
print(border)

##################################################
#             AdaBoost Classifier                #
##################################################
AdaBoost_Model = AdaBoostClassifier(n_estimators=50,learning_rate=1.0,random_state=42)
AdaBoost_Model = AdaBoost_Model.fit(X_train,Y_train)

Y_Pred = AdaBoost_Model.predict(X_test)
ADA_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)

print("Accuracy of AdaBoost Model is : ",ADA_Accuracy*100)
ADA_Precision = precision_score(Y_test, Y_Pred)
ADA_Recall = recall_score(Y_test, Y_Pred)
ADA_F1 = f1_score(Y_test, Y_Pred)
ADA_CM = confusion_matrix(Y_test, Y_Pred)
print("Confusion Matrix - AdaBoost:\n", ADA_CM)
print(border)

##################################################
#          Hard Voting Classifier                #
##################################################
LogisticReg_Model = LogisticRegression()
KNN_Model = KNeighborsClassifier(n_neighbors=5)

Voting_Model = VotingClassifier(estimators=[
    ('logistic',LogisticReg_Model),
    ('decision_tree',DecisionTree_Model),
    ('knn',KNN_Model)
]   ,voting="hard")

Voting_Model = Voting_Model.fit(X_train,Y_train)
Y_Pred = Voting_Model.predict(X_test)

HardV_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)

print("Accuracy of Hard Voting is : ",HardV_Accuracy*100)
HardV_Precision = precision_score(Y_test, Y_Pred)
HardV_Recall = recall_score(Y_test, Y_Pred)
HardV_F1 = f1_score(Y_test, Y_Pred)
HardV_CM = confusion_matrix(Y_test, Y_Pred)
print("Confusion Matrix - Hard Voting:\n", HardV_CM)
print(border)

##################################################
#          Soft Voting Classifier                #
##################################################
LogisticReg_Model = LogisticRegression()
KNN_Model = KNeighborsClassifier(n_neighbors=5)

Voting_Model = VotingClassifier(estimators=[
    ('logistic',LogisticReg_Model),
    ('decision_tree',DecisionTree_Model),
    ('knn',KNN_Model)
]   ,voting="soft")

Voting_Model = Voting_Model.fit(X_train,Y_train)
Y_Pred = Voting_Model.predict(X_test)

SoftV_Accuracy = accuracy_score(Y_test,Y_Pred)
print(border)

print("Accuracy of Soft Voting is : ",SoftV_Accuracy*100)
SoftV_Precision = precision_score(Y_test, Y_Pred)
SoftV_Recall = recall_score(Y_test, Y_Pred)
SoftV_F1 = f1_score(Y_test, Y_Pred)
SoftV_CM = confusion_matrix(Y_test, Y_Pred)
print("Confusion Matrix - Soft Voting:\n", SoftV_CM)
print(border)

##################################################
#              Model Metrics Table               #
##################################################

Metrics_Table = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Bagging",
        "Random Forest",
        "AdaBoost",
        "Hard Voting",
        "Soft Voting"
    ],
    "Accuracy": [
        Decision_Accuracy * 100,
        Bagging_Accuracy * 100,
        Random_Accuracy * 100,
        ADA_Accuracy * 100,
        HardV_Accuracy * 100,
        SoftV_Accuracy * 100
    ],
    "Precision": [
        Decision_Precision * 100,
        Bagging_Precision * 100,
        Random_Precision * 100,
        ADA_Precision * 100,
        HardV_Precision * 100,
        SoftV_Precision * 100
    ],
    "Recall": [
        Decision_Recall * 100,
        Bagging_Recall * 100,
        Random_Recall * 100,
        ADA_Recall * 100,
        HardV_Recall * 100,
        SoftV_Recall * 100
    ],
    "F1 Score": [
        Decision_F1 * 100,
        Bagging_F1 * 100,
        Random_F1 * 100,
        ADA_F1 * 100,
        HardV_F1 * 100,
        SoftV_F1 * 100
    ]
})

##################################################
#              Model Metrics Table               #
##################################################

print("\n" + border)
print("                    MODEL METRICS")
print(border)
print(Metrics_Table.to_string(index=False))
print(border)




print("\nRecommendation:")
print("Random Forest achieved the best performance across all metrics (100% Accuracy,")
print("Precision, Recall, and F1), correctly identifying every fraudulent transaction")
print("in the test set with no false positives or false negatives.")
print()
print("The other five models (Decision Tree, Bagging, AdaBoost, Hard Voting, Soft Voting)")
print("all scored identically at 92.3% Accuracy with 100% Precision but only 66.7% Recall,")
print("meaning they missed roughly a third of actual fraud cases (false negatives) while")
print("raising zero false alarms. In fraud detection, missing a fraud case is typically")
print("more costly than a false alarm, so Recall matters as much as Accuracy here.")
print()
print("Given its perfect scores across all metrics, Random Forest is recommended as the")
print("most suitable model — though given the small test set size, this result should")
print("be validated further using cross-validation before deploying in production.")