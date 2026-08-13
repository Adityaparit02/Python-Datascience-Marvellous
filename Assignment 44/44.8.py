import pandas as pd
import matplotlib.pyplot as plt


border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)

df['Total'] = df.sum(axis=1 , numeric_only= True)



##############################################################
#           Plot Line Graph For One Element in Data Frame                      #
##############################################################
Amit = df[df['Name'] == 'Amit']

plt.plot(
    ['Math' , 'Science' , 'English'],
    Amit[['Math' , 'Science' , 'English']].values[0],
    marker = 'o'
)


plt.xlabel("Course Subjects")
plt.ylabel("Marks")

plt.title("Amit's Marks Graph")

plt.show()
