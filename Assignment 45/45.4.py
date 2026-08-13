import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt


border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Gender' : ['Male','Male','Female'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)


df['Total'] = df.sum(axis=1,numeric_only=True)

##############################################################
#          Extracting Data of "Sagar" in Sagar               #
##############################################################
Sagar = df[df['Name'] == 'Sagar']



##############################################################
#          Plotting a Pie Chart.                             #
##############################################################
plt.pie(
    Sagar[['Math' ,'Science' ,'English']].values[0],
    labels=['Math','Science','English'],
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Sagar's Marks")
plt.show()