from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

border = "*" * 70
border2 = "-"*70
########################################################
#           Data Loading
########################################################
Data = [
    {"Study Hours" : 1 , "Marks" : 50},
    {"Study Hours" : 2 , "Marks" : 55},
    {"Study Hours" : 3 , "Marks" : 60},
    {"Study Hours" : 4 , "Marks" : 65},
    {"Study Hours" : 5 , "Marks" : 70}
]

########################################################
#           Data to DataFrame
########################################################
df = pd.DataFrame(Data)

X = df[['Study Hours']]
Y = df['Marks']

########################################################
#           Splitting Data
########################################################
X_Train , X_Test , Y_Train , Y_Test = train_test_split(X,Y, random_state=42,test_size=0.5)



########################################################
#           Model Creation and Training
########################################################
Model = LinearRegression()
Model = Model.fit(X_Train,Y_Train)


########################################################
#           Model Testing
########################################################
Y_Pred = Model.predict(X_Test)


print(border2)
print("Model Accuracy : ")
R2 = r2_score(Y_Test,Y_Pred)
print(border)
print(border)
print("R2 Score is : ",R2)
print(border)

MSE = mean_squared_error(Y_Test,Y_Pred)

print("MSE is : ",MSE)
print(border2)
print(border2)


########################################################
#          Print Coeeficcient and Intercept
########################################################
print("Coefficient is :")
print(Model.coef_)
print(border)

print("Intercept is :")
print(Model.intercept_)

print(border2)
print(border2)

########################################################
#          Predict New Value
########################################################

X_New = (
    pd.DataFrame({"Study Hours": [6]})
)

Predicted_Value = Model.predict(X_New)

print(f"If Someone Studies for {X_New['Study Hours'][0]} Hours He will get {Predicted_Value} Marks")
print(border2)
print(border2)