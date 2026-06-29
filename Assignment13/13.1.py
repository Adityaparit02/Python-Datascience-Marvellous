from Lib_13 import RectangleArea

def main():
    a=int(input("Enter length: "))
    b=int(input("Enter Breadth: "))
    c=RectangleArea(a,b)
    print("Area of rectangle is :",c )

if __name__=="__main__":
    main()