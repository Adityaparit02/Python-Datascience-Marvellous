def divisibility(n):
    if n%3==0 and n%5!=0:
        print(n,"is divisible by 3 and not by 5")
    elif n%3==0 and n%5==0:
        print(n,"is divisible by 3 and by 5")
    elif n%3!=0 and n%5==0:
        print(n,"is not divisible by 3 and is divisible by 5")



def main():
    a=int(input("print enter your number:"))
    divisibility(a)

if __name__=="__main__":
    main()