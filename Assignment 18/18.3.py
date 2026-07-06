from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter Value {i} : "))
        arr.append(value)
    return arr

minimun= lambda n,m: m if m<n else n

def main():
    no_elements=int(input("Enter Number of elements to enter in List: ")) 
    listx=listmaker(no_elements)
    RData=reduce(minimun,listx)

    print(f"The minimun value in {listx} is {RData}")

if __name__=="__main__":
    main()   