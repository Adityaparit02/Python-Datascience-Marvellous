import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


###############################################################################
# R E A D   D A T A
# Function : ReadData()
# Input    : FileName
# Return   : X_test, Y_test, Model
###############################################################################
def ReadData (FileName):
    df = pd.read_csv(FileName)
    return CleanData(df)



###############################################################################
# C L E A N   D A T A
# Function : CleanData()
# Input    : df
# Return   : X_test, Y_test, Model
###############################################################################
def CleanData(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,random_state=42,test_size=0.3) 

    Model = LinearRegressionmodel(X_train,  Y_train)

    return X_test,Y_test , Model


###############################################################################
# L I N E A R   R E G R E S S I O N
# Function : LinearRegressionmodel()
# Input    : X_train, Y_train
# Return   : Model
###############################################################################
def LinearRegressionmodel(X_train,Y_train,):
    Model = LinearRegression()
    Model = Model.fit(X_train,Y_train)

    return Model
    


###############################################################################
# A C C U R A C Y   C A L C U L A T I O N
# Function : Accuracycalculate()
# Input    : Model, X_test, Y_test
# Return   : Y_pred
###############################################################################
def Accuracycalculate(Model, X_test, Y_test):
    Y_pred = Model.predict(X_test)
    Accuracy = r2_score(Y_pred,Y_test)
    print("-" *70)
    print("accuracy is : ",Accuracy*100)
    print("-" *70)

    return Y_pred


###############################################################################
# P R I N T   D A T A
# Function : printdata()
# Input    : ypred, ytest
# Return   : None
###############################################################################
def printdata(ypred, ytest):

    print("\nPredicted\tActual")
    print("-------------------------")

    for predicted, actual in zip(ypred, ytest):
        print(f"{predicted:.2f}\t\t{actual:.2f}")


###############################################################################
# M A I N   F U N C T I O N
# Function : main()
# Input    : csv file
# Return   : None
###############################################################################
def main():
    X_test, Y_test, Model = ReadData("Advertising.csv")

    Y_pred = Accuracycalculate(Model, X_test, Y_test)

    printdata(Y_pred,Y_test)


###############################################################################
# S T A R T   O F   P R O G R A M
###############################################################################
if __name__ == "__main__":
    main()