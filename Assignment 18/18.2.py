from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter Value {i} : "))
        arr.append(value)
    return arr
    
maximum=lambda m,n : m if m>n else n

def main():
    no_elements=int(input("Enter number of Elements to Enter in List: "))
    listx=listmaker(no_elements)
    RData=reduce(maximum,listx)
    print(f"Maximum value in {listx} is {RData}")

if __name__=="__main__":
    main()