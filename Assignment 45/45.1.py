import pandas as pd
from sklearn.preprocessing import MinMaxScaler


border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)

scaler = MinMaxScaler()

print(border)
print("Original Data : ")
print(border)
print(df)
print(border)


Test_Data = df


print(border)
print("Scaling Performed Successfully...")
print(border)

print("Scaled Math Column Updated : ")
print(border)

##############################################################
#           Scaling Math column using MinMaxScaler           #
##############################################################

Test_Data['Scaled Data'] = scaler.fit_transform(df[['Math']])

print(Test_Data)
print(border)
print(border)
