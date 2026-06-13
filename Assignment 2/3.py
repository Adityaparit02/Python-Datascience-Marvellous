
#3. id() : id() function returns the unique identity (memory address) of an object. 
# This helps understand how Python manages memory and object refrences.
#  Yes, the value returned by id() is same for two variables holding same values as;
# a. variables store refrences, not values
# b. immutable objects may share memory

a=10                     #immutable variables
b=10
print("address of a is:",id(a))
print("address of b is:",id(b))