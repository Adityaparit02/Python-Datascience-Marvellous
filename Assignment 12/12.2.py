from Library_12 import GetFcators

def main():
    a=int(input("Give your number : "))
    b=GetFcators(a)
    print("Factors of ", a, "are",b)
if __name__=="__main__":
    main()