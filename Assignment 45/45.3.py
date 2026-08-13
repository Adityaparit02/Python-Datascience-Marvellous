import pandas as pd
from sklearn.preprocessing import OneHotEncoder


border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Gender' : ['Male','Male','Female'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)


df['Total'] = df.sum(axis=1,numeric_only=True)

print("Original Data : ")
print(border)
print(df)
print(border)
print(border)



##############################################################
#          Grouping Data as per Gender                       #
##############################################################
Gender_Sorted = df.groupby('Gender')

print("Sorted Data as Per Gender : ")
print(border)

for gender , data in Gender_Sorted:
    print(border)
    print("Gender : ", gender)

    print(data)

print(border)
print(border)



##############################################################
#          Calculating the Average marks of each Gender      #
##############################################################
Gender_Average = df.groupby('Gender')['Total'].mean()
print("Average Marks of Each Gender :")
print(border)

print(Gender_Average)

print(border)
print(border)
