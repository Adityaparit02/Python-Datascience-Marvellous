evencheck= lambda x : True if x % 2==0 else False

def main():
    a=int(input("Enter number :"))
    b=evencheck(a)
    print(b)

if __name__=="__main__":
    main()