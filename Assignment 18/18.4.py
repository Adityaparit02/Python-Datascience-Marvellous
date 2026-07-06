def listmaker(n):
    arr=list()
    for i in range(1,n+1):
        value=int(input(f"Enter Value {i} : "))
        arr.append(value)

    return arr


def element_search(listx,n):
    count=0
    for value in listx:
        if value==n:
            count=count+1
    return count



def main():
    No_elements=int(input("Enter number of elements to add in list : "))
    listx=listmaker(No_elements)

    element_to_search=int(input(f"Enter element to search in {listx} this list : "))
    count_element=element_search(listx,element_to_search)
    print(f"The value {element_to_search} has arrived {count_element} times in the list {listx}")

if __name__=="__main__":
    main()