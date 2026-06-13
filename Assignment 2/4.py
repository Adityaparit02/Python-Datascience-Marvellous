#The purpose of getsizeof():
#getsizeof() function returns the memory size (in bytes) occupied by an object.

#Diffrent memory size for diffrent data types :
#coz diffrent data types store diffrent memory sizes because their object structures and
#storage requirements are diffrent , python does not define a single 
#fixed size for all objects.

import sys

a=1
b=1.5
c=True
d="Hello, Aditya"

print("size of a :",sys.getsizeof(a))
print("size of a :",sys.getsizeof(b))
print("size of a :",sys.getsizeof(c))
print("size of a :",sys.getsizeof(d))





