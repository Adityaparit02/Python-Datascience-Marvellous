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
#           Graph Plot based on Total Makrks of Students                      #
##############################################################
plt.bar(df['Name'], df['Total'] ,color = 'lightblue' ,edgecolor ='black',)

plt.xlabel("Name of Students")
plt.ylabel("Total Marks")

plt.title("Student Names v/s Marks")

plt.show()