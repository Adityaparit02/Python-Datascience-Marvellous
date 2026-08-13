import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import numpy as np


border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Gender' : ['Male','Male','Female'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)


df['Total'] = df.sum(axis=1,numeric_only=True)

print(border)
print("Original Data : ")
print(border)
print(df)
print(border)
print(border)

######################################################################
# Updating Student status as Pass/ Fail in new Column Named 'Status  #
######################################################################
print("Updated Status of Pass/ Fail :")
print(border)
df['Status'] = np.where(df['Total'] >=250 , 'Pass' , 'Fail')

print(df)

print(border)
print(border)


##############################################################
#          Counting Students who Passed                      #
##############################################################
PassCount = 0
for Status in df['Status']:
    if Status == 'Pass':
        PassCount = PassCount +1


print("Total Number of Students Passed : ",PassCount)
print(border)

