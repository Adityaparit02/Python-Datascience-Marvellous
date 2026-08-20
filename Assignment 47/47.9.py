from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split

########################################################
#                    Data
########################################################
Data = [
    {"Study Hours" : 1 ,"SleepHours": 7, "Marks" : 50},
    {"Study Hours" : 2 ,"SleepHours": 6, "Marks" : 55},
    {"Study Hours" : 3 ,"SleepHours": 7, "Marks" : 60},
    {"Study Hours" : 4 ,"SleepHours": 7, "Marks" : 65},
    {"Study Hours" : 5 ,"SleepHours": 8, "Marks" : 70},
]



########################################################
#               DataFrame Creation
########################################################
df = pd.DataFrame(Data)

X = df[["Study Hours","SleepHours"]]
Y = df["Marks"]

########################################################
#                 Train Test Split
########################################################
X_Train, X_Test , Y_Train , Y_Test = train_test_split(X,Y,test_size=0.5,random_state=42)


########################################################
#              Model Creation & Training
########################################################
Model = LinearRegression()
Model = Model.fit(X_Train,Y_Train)



########################################################
#                    Prediction and Evaluation
########################################################
Y_Pred = Model.predict(X_Test)

r2 = r2_score(Y_Pred,Y_Test)

print("R2 Score is : ",r2)

MSE = mean_squared_error(Y_Pred,Y_Test)

print("Mean Squared Error is : ",MSE)


########################################################
#                  Coefficients and Intercept
########################################################
coefficients = Model.coef_

coefficient_1 = coefficients[0]
coefficient_2 = coefficients[1]

print("coefficient of Study Hours is : ",coefficient_1)
print("coefficient of Sleep Hours is : ",coefficient_2)
