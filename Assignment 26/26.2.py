class Circle():
    pi = 3.14

    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0

    def accept(self):
        no=int(input("Enter radius : "))
        self.radius = no

    def calculatearea(self):
        self.area = Circle.pi * self.radius * self.radius

    def calculatecircumference(self):
        self.circumference = 2 * Circle.pi * self.radius

    def display(self):
        print(f"Radius = {self.radius}")
        print(f"Area is : {self.area}")
        print(f"Circumference is : {self.circumference}")

def main():
    obj1 = Circle()
    obj2 = Circle()
    print("#"*20 ,"Object 1", "*" * 20)
    print()
    obj1.accept()
    obj1.calculatearea()
    obj1.calculatecircumference()
    obj1.display()
    
    print()
    
    print()
    print("#"*20 ,"Object 2", "*" * 20)
    print()
    obj2.accept()
    obj2.calculatearea()
    obj2.calculatecircumference()
    obj2.display()

if __name__ =="__main__":
    main()