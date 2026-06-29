#1.to check prime

def isPrimex(n):
    if n<=1:
        return False
    
    for i in range(2,n-1):
        n%i==0
        return  False
    
    
    return True


#2.To print count of digits in number
def DigitCount(n):
    n=str(n)
    return len(n)


#3.sum of digits
def SumDigits(n):
    sum=0
    n=str(n)
    for i in range (0,len(n)):
        sum=sum+int(n[i])
    return sum

#4.reverse of number
def ReverseNumber(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse
    
#5 palindrome
def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False