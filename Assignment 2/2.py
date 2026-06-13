#Program to display difference in id() function.


#Immutable
a=10
b=10
print("Location of a:",id(a))
print("Location of b:",id(b))


#Mutable
a1=[10]
b1=[10]
print("Location of a1:",id(a1))
print("Location of b1:",id(b1))



#The location of a and b comes same whereas the 
# location of a1 and b1 comes diffrent coz python reuses mutable objects
#A list is immutable so its not reused and hence it shows diffrent adresses for
#both a1 and b1 and both variables a and b point to the same value hence the address is same. 