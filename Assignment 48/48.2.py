import numpy as np

border = "-" * 70 
X = np.array([1,2,3,4,5])
Y = np.array([3,4,2,4,5])


########################################################
#                 Calculate Mean
########################################################
sum =0
for n in X :
    sum = sum + n

X_Mean = sum /len(X)

sum =0

for n in Y :
    sum = sum + n

Y_Mean = sum /len(Y)


########################################################
#                 Calculate Slope
########################################################
Numerator = ((X - X_Mean) * (Y - Y_Mean)).sum()
Denominator = ((X - X_Mean) **2).sum()

slope = Numerator/Denominator
print(border)
print ("Slope is : ",slope)
print(border)


########################################################
#                 Calculate Intercept
########################################################
Intercept = Y_Mean - slope * X_Mean
print("Intercept is :",Intercept)
print(border)

########################################################
#                 Calculate Predictions
########################################################
Y_Predicted = slope * X + Intercept
print("Predicted Values :")

for i in range(len(X)):
    print(f"X = {X[i]}  →  Predicted Y = {Y_Predicted[i]:.2f}")

X_New = 6

New_Y_Predicted = slope * X_New + Intercept
print(border)
print(border)

print("Predicted value for X = 6 is :", New_Y_Predicted)
print(border)


########################################################
#                 R2 Score
########################################################

SS_Res = (( Y - Y_Predicted) **2).sum()
SS_Tot = ((Y - Y_Mean) **2 ).sum()

R2 = 1 - (SS_Res / SS_Tot)

print("R2 Score is : ",R2)
print(border)



########################################################
#                 Mean Squared Error
########################################################
MSE = 1/len(X) * ((Y - Y_Predicted) **2).sum()

print("MSE is : ",MSE)
print(border)
