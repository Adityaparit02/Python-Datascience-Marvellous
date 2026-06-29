#1. Area of rectangle
def RectangleArea(l,b):
    return l*b

#2.Areea of circle
def CircleArea(r):
    return 3.14*r*r


#3.Perfect number
def PerfectNumber(n):
    sum=0
    a=list()
    for i in range (1,n):
        if n%i==0:
            a.append(i)


    for i in range (len(a)):
        sum=sum+a[i]

    if sum == n:
        return True
    else:
        return False
    
#4.Accepts one number and gives its binary
def BinaryConverter(n):
    a=list()
    while n>0:
        a.append(n%2)
        n=n//2

    binary = ""
    for i in range(len(a)-1, -1, -1):
        binary = binary + str(a[i])

    return binary

#5. Grade Displayer
def GradeChecker(mks):
    if mks >= 75 and mks<=100:
        print("Distinction")
    elif mks>=60 and mks <=75:
        print("First Class")
    elif mks >=50 and mks <=60:
        print("Second Class")
    elif mks >=0 and mks<=50:
        print("Fail")
    else:
        print("Enter appropriate value please.")