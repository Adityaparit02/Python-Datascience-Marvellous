import threading

def small_characters(n):
    lower_case = 0
    lowercase_list=list()
    for i in range(len(n)):
        if n[i].islower():
            lower_case = lower_case+1
            lowercase_list.append(n[i])

    print(f"The lowercase characters are : {lowercase_list}")
    print(f"The number of lowercase characters is: {lower_case}")


def capital_characters(n):
    upper_case= 0
    uppercase_list=list()
    for i in range(len(n)):
        if n[i].isupper():
            upper_case=upper_case+1
            uppercase_list.append(n[i])

    print(f"The uppercase characters are : {uppercase_list}")
    print(f"The number of uppercase characters is: {upper_case}")


def numbers(n):
    numbers=0
    number_list=list()
    for i in range(len(n)):
        if n[i].isdigit():
            numbers=numbers+1
            number_list.append(n[i])

    print(f"The digit characters are : {number_list}")
    print(f"The number of digit characters is: {numbers}")


def main():
    value=input("Enter your string : ")

    t1=threading.Thread(target=small_characters,args=(value,))
    t2=threading.Thread(target=capital_characters,args=(value,))
    t3=threading.Thread(target=numbers,args=(value,))

    t1.start()
    t2.start()
    t3.start()
    
    t2.join()
    t1.join()
    t3.join()


if __name__=="__main__":
    main()