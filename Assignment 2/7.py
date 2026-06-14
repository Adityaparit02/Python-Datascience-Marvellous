#7.Why does the input() function always return a string? How can you convert the input to another data type?

#The input() function reads data entered from keyboard as text. Since 
#everything typed by the user initially comes in form of characters.
#The keyboard sends characters to the program . Python cannot automatically know whether the input
#should be int,float,bool,str. So to avoid wrong assumptions , input() always return a string
#and lets the programmer decide the required data type.


#We can convert it by doing typecasting, Typecasting is a way in which the variable to which the input is taken
#It can be temporarily changing its data type to the data type assigned by the user.

#Eg:

input1=input("Enter first number:")         #Input taken as string
input2=input("Enter second number:")        #Input taken as string

print(type(input1))                            #Output will be <class 'str'>
print(type(input2))                            #Output will be <class 'str'>

input1=int(input1)                          #Typecasting to integer
input2=int(input2)                          #Typecasting to integer

print("Addition of",input1,"and",input2,"is:",input1+input2)

print(type(input1))                            #Output will be <class 'int'>
print(type(input2))                            #Output will be <class 'int'>