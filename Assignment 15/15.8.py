divisible_3_5 = lambda n : n%3 == 0 and n%5 ==0

def listmaker(n):
    arr=list()
    for i in range (n):
        a= int(input("enter value: "))
        arr.append(a)

    return list(arr)
    

def main():
    no_elements=int(input("Enter no of elements to enter :"))
    listx=listmaker(no_elements)
    FData= filter(divisible_3_5,listx)
    print("The values divisible by 3 and 5 are :" ,list(FData))

if __name__=="__main__":
    main()