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
df.fillna(df.mean(numeric_only=True),inplace= True)



print(border)
print("The Original Data : ")
print(border)
print(df)
print(border)
print(border)

##############################################################
#           Drop English Column from DataFrame                      #
##############################################################
print("English Column Deleted Successfully...")
print(border)
print("New Data : ")
print(border)
New = df.drop(columns=['English'])
print(New)
print(border)
print(border)
