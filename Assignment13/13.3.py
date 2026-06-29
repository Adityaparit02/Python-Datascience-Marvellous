from Lib_13 import PerfectNumber

def main():
    a= int (input("Enter your number :"))
    
    if PerfectNumber(a):
        print (a,"is Perfect number")
    else :
        print(a,"is not a perfect number")

if __name__=="__main__":
    main()