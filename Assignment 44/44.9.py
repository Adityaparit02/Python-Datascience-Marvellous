import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  


border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [np.nan,90,78],
    'Science' : [92,np.nan,80],
    'English' : [75,85,82]}
)

df['Total'] = df.sum(axis=1 , numeric_only= True)

print(border)
print("Original Data : ")
print(border)
print(df)
print(border)
print(border)

##############################################################
#           Remove Null Values                      #
##############################################################
print("Null Values Removal Completed Successfully...")
print(border)
print("Updated Data : ")
print(border)
df_Updated = df.fillna(df.mean(numeric_only=True))
print(df_Updated)

print(border)
print(border)
