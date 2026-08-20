from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt


########################################################
#                    Data Loading
########################################################

Data = [
    {"Experience":1 , "Salary" : 20000},
    {"Experience":2 , "Salary" : 25000},
    {"Experience":3 , "Salary" : 30000},
    {"Experience":4 , "Salary" : 35000},
    {"Experience":5 , "Salary" : 40000},
]

########################################################
#                 DataFrame Creation
########################################################
df = pd.DataFrame(Data)

X = df[["Experience"]]
Y = df["Salary"]

########################################################
#                    Data Splitting
########################################################
X_train , X_test , Y_train , Y_test = train_test_split(X,Y,train_size=0.5,random_state=42)


########################################################
#              Model Creation and Training
########################################################
Model = LinearRegression()
Model = Model.fit(X_train,Y_train)


########################################################
#                  Model Prediction
########################################################
Y_Pred = Model.predict(X_test)


########################################################
#                    R2 Score
########################################################
r2 = r2_score(Y_test,Y_Pred)
print("-"*70)
print("r2 score ",r2)
print("-"*70)


########################################################
#              Mean Squared Error
########################################################
mse = mean_squared_error(Y_test,Y_Pred)
print("mse :",mse)

print("-"*70)
print("-"*70)


########################################################
#                 New Value Prediction
########################################################
new_X = pd.DataFrame({
    "Experience" : [6]
    })

Y_predicted = Model.predict(new_X)

print("Predicted Salary for 6 Years Experience :",Y_predicted)
print("-"*70)

########################################################
#               Regression Line Prediction
########################################################
Y_Line = Model.predict(X)

########################################################
#                  Plotting Graph
########################################################

plt.scatter(
    X,
    Y,
    label="Actual Data"
)

plt.plot(
    X,
    Y_Line,
    label="Regression Line"
)

plt.xlabel("Experience (Years)")

plt.ylabel("Salary")

plt.title("Experience vs Salary")

plt.legend()

plt.show()