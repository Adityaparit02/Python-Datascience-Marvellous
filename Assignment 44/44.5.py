import pandas as pd
border = "-"*70

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)

df['Total'] = df.sum(axis=1 , numeric_only= True)

Old_Name = 'Pooja'
New_Name = 'Puja'

print(border)
print("Previous Data : ")
print(border)
print(df)
print(border)
print(border)

##############################################################
#          Replace Old Value with New Value                     #
##############################################################
df['Name'] = df['Name'].replace(Old_Name , New_Name)
print(f"Name Successfully Changed from {Old_Name} to {New_Name}" )
print(border)
print(df)
print(border)
print(border)

