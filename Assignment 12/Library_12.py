#1.To check vowel
def VowelCheck(c):
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
        return True
    else:
        return False



#2.To print factors
def GetFcators(n):
    a=list()

    for i in range (1,n+1):
        if n%i==0:
            a.append(i)
        else:
            pass

    return list(a)



#3.Calculator

def calculator(n,m):
    return n+m,n-m,n*m,n//m
    


#4.List generator

def listgenerator(n):
    a=list()
    for i in range(1,n+1):
        a.append(i)
    return list(a)



#5.Generate list in reverse
def listgeneratorREV(n):
    a=list()
    b=list()
    for i in range(1,n+1):
        a.append(i)

    for i in range (len(a),-1,-1):
        b.append(i)

    return list(b)