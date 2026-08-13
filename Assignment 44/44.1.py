import pandas as pd
border = "-"*30

df = pd.DataFrame(
    {'Name' : ['Amit','Sagar','Pooja'] ,
    'Math' : [85,90,78],
    'Science' : [92,88,80],
    'English' : [75,85,82]}
)
##############################################################
#           Display Shape of Data Frame                      #
##############################################################
print(border)
print("Shape of Data Frame is : ")
print(df.shape)
print(border)
print(border)

##############################################################
#           Display Columns of Data Frame                      #
##############################################################
print("Columns in Data Frame are : ")
print(df.columns)
print(border)
print(border)

##############################################################
#           Display Data Types of Columns in Data Frame                      #
##############################################################
print("Data Types of Column are :")
print(df.dtypes)
print(border)
print(border)
