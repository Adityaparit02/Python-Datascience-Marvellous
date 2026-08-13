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

Test_Data = df.copy()


print(border)
print("Original Data : ")
print(border)
print(df)
print(border)
print(border)

encode= OneHotEncoder(sparse_output=False)


##############################################################
#           One Hot Encoding of Gender Column                #
##############################################################
Encoded_Data = encode.fit_transform(df[['Gender']])

Encoded_Data = pd.DataFrame(
    Encoded_Data,
    columns=encode.get_feature_names_out(['Gender'])
)


##############################################################
#       Concating The Encoded data columns in DataFrame      #
##############################################################
Test_Data = pd.concat([Test_Data,Encoded_Data],axis=1)

print("Encoded Data using One Hot Encodeing (Gender Column Only)..")
print(border)
print("Updated Data : ")
print(border)
print(Test_Data)
print(border)
print(border)
