class Arithmetic():
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        self.value1 = int(input("Enter Value 1 : "))
        self.value2 = int(input("Enter Value 2 : "))

    def Addition(self):
        sum = self.value1 + self.value2
        return sum
    
    def Subtraction(self):
        sub =self.value1 - self.value2
        return sub
        
    def Multiplication(self):
        mul = self.value1 * self.value2
        return mul
        
    def Division(self):
        div = self.value1 / self.value2
        return div
    
def main():
    obj1 = Arithmetic() 
    obj2 = Arithmetic() 

    print("#"*20 ,"Object 1", "*" * 20)
    print()
    obj1.Accept()
    print(f"The Addition is : {obj1.Addition()}")
    print(f"The Substraction is : {obj1.Subtraction()}")
    print(f"The multiplication is : {obj1.Multiplication()}")
    print(f"The division is : {obj1.Division()}")

    print()
    
    print()
    print("#"*20 ,"Object 2", "*" * 20)
    print()

    obj2.Accept()
    print(f"The Addition is : {obj2.Addition()}")
    print(f"The Substraction is : {obj2.Subtraction()}")
    print(f"The multiplication is : {obj2.Multiplication()}")
    print(f"The division is : {obj2.Division()}")


if __name__ =="__main__":
    main()