###############################################################################
#
#                      K N N   C L A S S I F I E R
#
###############################################################################
# Project Name : Play Predictor
# Algorithm    : K-Nearest Neighbors Classification
# Description  : Predicts whether Play is possible based on
#                Weather and Temperature.
###############################################################################

import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt

###############################################################################
#                         K N N   A L G O R I T H M
###############################################################################
def KNNAlgorithm(X,Y,K=9):

    ############### Label Encoding
    le = LabelEncoder()

    ############### One-Hot Encoding
    X = pd.get_dummies(X, dtype=int)
    Columns = X.columns
    Y = le.fit_transform(Y)

    ############### Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    ############### Creating Model
    Model = KNeighborsClassifier(n_neighbors=K)

    ############### Training Model
    Model = Model.fit(X_train,y_train)

    ############### Prediction
    y_Pred = Model.predict(X_test)

    return y_Pred,y_test,Model,Columns




###############################################################################
#                         A C C U R A C Y
###############################################################################
def CheckAccuracy(y_test,y_Pred):
    ############## Accuracy
    Accuracy = accuracy_score(y_test,y_Pred)

    return Accuracy



###############################################################################
#                         P L A Y   P R E D I C T I O N
###############################################################################
def PredictPlay(Model, Weather, Temperature, Columns):

    ############### Creating Input
    NewData = pd.DataFrame({
        'Wether': [Weather],
        'Temperature': [Temperature]
    })

    ############### One-Hot Encoding
    NewData = pd.get_dummies(NewData, dtype=int)

    ############### Matching Columns
    NewData = NewData.reindex(columns=Columns, fill_value=0)

    ############### Prediction
    Prediction = Model.predict(NewData)

    if Prediction[0] == 1:
        print("Play : Yes")
    else:
        print("Play : No")


###############################################################################
#                         K   T U N I N G
###############################################################################
def KTuning():
    ############### Importing Data
    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    ############### Separating Data
    X = df[['Wether','Temperature']]                      
    Y = df['Play']
    
    ############### Checking for diffrent values of K
    for k in range (1,12):
        Y_PRED,Y_TEST,Model,Columns = KNNAlgorithm(X,Y,k)
        Accuracy = CheckAccuracy(Y_TEST,Y_PRED)
        print(f"The Accuracy for k = {k} is {Accuracy}")



###############################################################################
#                              M A I N
###############################################################################
def main():
    ############### Importing Data
    df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

    ############### Separating Data
    X = df[['Wether','Temperature']]                      
    Y = df['Play']

    Y_PRED,Y_TEST,Model,Columns = KNNAlgorithm(X,Y)

    print("\n" + "=" * 50)
    print("              P L A Y   P R E D I C T O R")
    print("=" * 50)

    print("\nWeather Options")
    print("-" * 30)
    print("1. Sunny")
    print("2. Rainy")
    print("3. Overcast")

    weather = input("\nEnter the weather : ")

    print("\nTemperature Options")
    print("-" * 30)
    print("1. Hot")
    print("2. Mild")
    print("3. Cool")

    temperature = input("\nEnter the temperature : ")

    print("\n" + "-" * 50)
    print("              P R E D I C T I O N")
    print("-" * 50)

    PredictPlay(Model, weather, temperature, Columns)

    print("\n" + "=" * 50)
    KTuning()





###############################################################################
#                              S T A R T
###############################################################################
if __name__ == "__main__":
    main()