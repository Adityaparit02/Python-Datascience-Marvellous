#Predict the output and explain reason for the error:
def fun():
    x=10
    print(x)
fun()
print(x)



#Output :

#10
#error(print(x)
#NameErroe: name 'x' is not defined


#The x=10 is the variable assigned inside the function fun()
#hence the variable can be only accessed inside the function fun()
#because its the local variable of the function.

