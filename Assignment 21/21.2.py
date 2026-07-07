import threading

def minimum(n):
    min_value=n[0]
    for value in n :
        if value < min_value:
            min_value=value

    print(f"Minimum value in list is : {min_value}")

def maximum(n):
    max_value=n[0]
    for value in n:
        if value> max_value:
            max_value=value

    print(f"Maximum value in list is : {max_value}")


def listmaker(n):
    arr=list()
    for i in range (1,n+1):
        value=int(input(f"Enter Value {i} : "))
        arr.append(value)
    print(f"The list is : {arr}")
    return arr


def main():
    no_elements=int(input("Enter number of elements to add in the list : "))
    listx=listmaker(no_elements)
    
    t1=threading.Thread(target=minimum,args=(list(listx),))
    t2=threading.Thread(target=maximum,args=(list(listx),))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()
    