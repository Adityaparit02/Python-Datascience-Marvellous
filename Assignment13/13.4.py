from Lib_13 import BinaryConverter

def main():
    a=int(input("Enter your number :"))
    b=BinaryConverter(a)
    print("Binary of ",a,"is",b)
if __name__=="__main__":
    main()