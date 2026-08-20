from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

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

R2 = r2_score(Y_Test,Y_Pred)

print("R2 Score is : ",R2)

MSE = mean_squared_error(Y_Test,Y_Pred)

print("MSE is : ",MSE)


########################################################
#          Print Coeeficcient and Intercept
########################################################
print("Coefficient is :")
print(Model.coef_)

print("Intercept is :")
print(Model.intercept_)