# ======================================================================
# Import Required Libraries
# ======================================================================
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,classification_report
import matplotlib.pyplot as plt
import seaborn as sns
border = "-"*70


# ======================================================================
# Load Dataset
# ======================================================================
df = pd.read_csv("breast-cancer-wisconsin.csv")


# ======================================================================
# Display Description of Dataset
# ======================================================================
print(border)
print("Discription of Data :")
print(df.describe())
print(border)

# ======================================================================
# Replace Missing Values with NaN
# ======================================================================
df.replace("?", np.nan, inplace=True)

# ======================================================================
# Display Number of Null Values
# ======================================================================
print(border)
print("Number of Null Values :")
print(df.isnull().sum())
print(border)


# ======================================================================
# Convert BareNuclei Column into Numeric Data
# ======================================================================
df['BareNuclei'] = pd.to_numeric(df['BareNuclei'], errors='coerce')


# ======================================================================
# Fill Missing Values with Median
# ======================================================================
print(border)
print("Filled Null Values with Median Successfully...")
df['BareNuclei'] = df['BareNuclei'].fillna(df['BareNuclei'].median())
print(border)

# ======================================================================
# Feature Correlation Visualization
# ======================================================================
print(border)
print("Feature Correlation Matrix :")

Correlation = df.corr(numeric_only=True)

print(Correlation)
print(border)

# ======================================================================
# Display Correlation Heatmap
# ======================================================================
plt.figure(figsize=(12, 8))

sns.heatmap(
    Correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()


# ======================================================================
# Remove Duplicate Rows
# ======================================================================
print(border)
print("Duplicate Rows Dropped Successfully...")
df.drop_duplicates(inplace=True)
print(border)


# ======================================================================
# Display Description of Dataset after EDA
# ======================================================================
print(border)
print("Dataset After Preprocessing :")
print(df.describe())
print(border)


# ======================================================================
# Separate Features and Target Variable
# ======================================================================
X = df.drop(columns=["CancerType"])
Y = df["CancerType"]

# ======================================================================
# Split Dataset into Training and Testing Data
# ======================================================================
X_Train , X_test , Y_Train , Y_Test = train_test_split(X,Y,train_size=0.7,random_state=42,stratify=Y)


# ======================================================================
# Create and Train Random Forest Classifier
# ======================================================================
Model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
Model = Model.fit(X_Train,Y_Train)

# ======================================================================
# Make Predictions on Test Data
# ======================================================================
Y_Pred = Model.predict(X_test)


# ======================================================================
# Calculate Accuracy of Model
# ======================================================================
print(border)
Accuracy = accuracy_score(Y_Test,Y_Pred)
print("Accuracy of Model is : ",Accuracy*100)
print(border)


# ======================================================================
# Display Confusion Matrix
# ======================================================================
print(border)
print("confusion Matrix:")
print(confusion_matrix(Y_Test,Y_Pred))
print(border)


# ======================================================================
# Calculate Precision Score
# ======================================================================
print(border)
print("Precision Score of Model is : ", precision_score(Y_Test,Y_Pred,pos_label=4))
print(border)

# ======================================================================
# Calculate Recall Score
# ======================================================================
print(border)
print("Recall Score of Model is :",recall_score(Y_Test,Y_Pred,pos_label=4))
print(border)


# ======================================================================
# Calculate F1 Score
# ======================================================================
print(border)
print("F1 Score of Model is : ",f1_score(Y_Test,Y_Pred,pos_label=4))
print(border)


# ======================================================================
# Display Complete Classification Report
# ======================================================================
print(border)
print("Classification Report :")
print(classification_report(Y_Test, Y_Pred))
print(border)

print(border)
print("Number of Trees : ", len(Model.estimators_))
print(border)
for i, tree in enumerate(Model.estimators_):
    print("Tree", i + 1)
    print("Number of Nodes :", tree.tree_.node_count)
    print("Maximum Depth :", tree.tree_.max_depth)
    print()