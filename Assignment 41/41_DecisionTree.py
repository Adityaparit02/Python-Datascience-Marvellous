import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("WinePredictor.csv")

X = df[["Alcohol", "Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"]]
y = df["Class"]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier()

model.fit(X_train,y_train)
ypred = model.predict(X_test)
accuracy = accuracy_score(y_test,ypred)
print("Accuracy :",accuracy*100 )

print(df.isnull().sum())  # just to demonstrate no missing values