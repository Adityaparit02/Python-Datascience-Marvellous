from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter value {i}: "))
        arr.append(value)

    return arr

        
def evensort(n):
    if n%2==0:
        return n
    
square_Of_nos= lambda n : n**2

addition = lambda n,m : n+m

def main():
    no_elements=int(input("Enter number of elements to enter in list : "))
    listx=listmaker(no_elements)

    FData=list(filter(evensort,listx))
    MData=list(map(square_Of_nos,FData))
    RData=reduce(addition,MData)

    print(f"The List is : {listx}")
    print(f"The List after filter is : {FData}")
    print(f"The List after map is : {MData}")
    print(f"The List after reduce is : {RData}")

if __name__=="__main__":
    main()