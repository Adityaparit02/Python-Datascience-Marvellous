import pandas as pd
border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)

df['Total'] = df.sum(axis=1 , numeric_only= True)

print(border)
print("Previous Data : ")
print(df)
print(border)
print(border)


##############################################################
#      Sort Values in Descending order of Total Column                      #
##############################################################
sorted = df.sort_values(by='Total',ascending=False)
df = sorted
print(df)

print("Data Sorted Successfuly Based on Total ...")
print(border)
print(border)



