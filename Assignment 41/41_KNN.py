import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

####################################################################################################################
#               Read CSV File
####################################################################################################################
df = pd.read_csv("WinePredictor.csv")


####################################################################################################################
#               Check for null Values
####################################################################################################################
print(df.isnull().sum())  
df.dropna(inplace=True)


####################################################################################################################
#               Splitting Dataset
####################################################################################################################
X = df.drop(columns=['Class'])                      #leaving class everything else considered as X 
Y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
Scaler = StandardScaler()

X_train = Scaler.fit_transform(X_train)
X_test = Scaler.transform(X_test)


####################################################################################################################
#               HyperParameter Tuning
####################################################################################################################
accuracy_scores = []

for n in range(1,21):
    Model = KNeighborsClassifier(n_neighbors=n)
    Model.fit(X_train, y_train)
    y_pred_Result = Model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_Result)

    accuracy_scores.append([n, accuracy])

for values in accuracy_scores:
    print(values)

K_values = []
Accuracy_values = []

for values in accuracy_scores:
    K_values.append(values[0])
    Accuracy_values.append(values[1] * 100)

#######     GRAPHICAL REPRESENTATION OF HYPERPARAMETER TUNING
plt.figure(figsize=(8,5))
plt.plot(K_values, Accuracy_values, marker="o")
plt.title("KNN Hyperparameter Tuning")
plt.xlabel("Number of Neighbors (K)")
plt.ylabel("Accuracy (%)")

plt.xticks(range(1,21))
plt.ylim(0,100)

plt.grid(True)

plt.show()


####################################################################################################################
#               Training and Testing of Model
####################################################################################################################
Model = KNeighborsClassifier(n_neighbors=8)
Model = Model.fit(X_train,y_train)

Y_Pred_Results = Model.predict(X_test)
Accuracy = accuracy_score(Y_Pred_Results,y_test)

print("Accuracy Scores is : ",Accuracy*100)

