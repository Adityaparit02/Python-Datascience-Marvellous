from functools import reduce

class Numbers ():
    def __init__(self,value):
        self.value = value

    def ChkPrime(self):
        if self.value <= 1 :
            return False
        
        else:
            for i in range(2,self.value):
                if self.value % i == 0 :
                    return False
                
        return True
    
    def ChkPerfect(self):
        add=lambda m,n : m+n
        self.arr = list()
        for i in range (1,self.value+1):
            if self.value % i  == 0 :
                self.arr.append(i)
        RData= reduce(add,self.arr[:-1])

        if self.value == RData:
            return True
        
        else:
            return False


    def Factors(self):
        self.arr = list()
        for i in range (1,self.value+1):
            if self.value % i  == 0 :
                self.arr.append(i)

        return self.arr
    
    def SumFactors(self):
        add=lambda m,n : m+n
        self.arr = list()
        for i in range (1,self.value+1):
            if self.value % i  == 0 :
                self.arr.append(i)

        RData= reduce(add,self.arr)

        return RData


def main():
    obj1 = Numbers(int(input("Enter Value : ")))
    obj2 = Numbers(int(input("Enter Value : ")))

    print()
    print("#"*20 ,"Object 1", "*" * 20)
    print()
    print(f"The result for testing prime : {obj1.ChkPrime()}")
    print(f"The result for testing perfect : {obj1.ChkPerfect()}")
    print(f"The factors are : {obj1.Factors()}")
    print(f"The sum of factors is : {obj1.SumFactors()}")
    print()
    
    print()
    print("#"*20 ,"Object 2", "*" * 20)
    print()

    print(f"The result for testing prime : {obj2.ChkPrime()}")
    print(f"The result for testing perfect : {obj2.ChkPerfect()}")
    print(f"The factors are : {obj2.Factors()}")
    print(f"The sum of factors is : {obj2.SumFactors()}")


if __name__=="__main__":
    main()