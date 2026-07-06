from functools import reduce

def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        no=int(input(f"Enter Value {i} : "))
        arr.append(no)
    return arr

addition= lambda n,m : n+m


def main():
    no_elements=int(input("Enter number of Elements to Enter: "))
    listx=listmaker(no_elements)
    RData=reduce(addition,listx)
    print(f"Addition of {listx} is {RData}")

if __name__=="__main__":
    main()
