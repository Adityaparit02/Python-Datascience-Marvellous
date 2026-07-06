import Arithmetic

def main():
    print(":::::::::::::::::Select Operation:::::::::::::::")
    print("1.Addition       2.Substraction          3.Multiplication            4.Division")
    inputx=int(input("Enter Operation Number: "))
    

    value= int(input("Enter first number :"))
    value2=int(input("Enter second number :"))

    
    if inputx==1:
        ret=Arithmetic.Add(value,value2)

    elif inputx==2:
        ret=Arithmetic.Sub(value,value2)

    elif inputx==3:
        ret=Arithmetic.Mult(value,value2)

    elif inputx==4:
        ret=Arithmetic.Div(value,value2)

    else :
        print("Invalid Input")

     
    


if __name__=="__main__":
    main()