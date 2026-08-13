import pandas as pd
border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)


##############################################################
#    Calculate Total Makrs and Add that Column in Data Frame                      #
##############################################################
df['Total'] = df.sum(axis=1 , numeric_only= True)
print(border)
print("The Total Marks of Each Students Calculated : ")
print(border)
print(df)
print(border)
print(border)

