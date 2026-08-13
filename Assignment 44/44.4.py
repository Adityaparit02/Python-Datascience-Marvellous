import pandas as pd
border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)

df['Total'] = df.sum(axis=1 , numeric_only= True)

##############################################################
#    Sort Students Who Have scored more than 85 in Science                      #
##############################################################
print(border)
print("Students Who Scored More Than 85 Marks in Science : ")
print(border)


print(df[df['Science'] > 85])
print(border)
print(border)
