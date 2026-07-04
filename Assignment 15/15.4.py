from functools import reduce


addition = lambda a,b : a+b 

def listmaker (n):
    arr=list()
    for i in range (n):
        a=int(input("Enter value: "))
        arr.append(a)

    return list (arr)

def main():
    no_elements= int (input("Enter no of elements to add in list :"))
    listx= listmaker(no_elements)
    RData= reduce(addition,listx)
    print("Addition of all values of list are : ", RData)

if __name__=="__main__":
    main()