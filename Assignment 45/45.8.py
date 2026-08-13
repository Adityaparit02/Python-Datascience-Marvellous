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
df['Status'] = np.where(df['Total'] >=250 , 'Pass' , 'Fail')



##############################################################
#          Taking Data of 'Math' in Maths                    #
##############################################################
Maths = df['Math']

##############################################################
#          Plotting Histogram of Maths Column                #
##############################################################
plt.hist(Maths,color='skyblue',edgecolor = 'black')
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Maths Marks")
plt.show()