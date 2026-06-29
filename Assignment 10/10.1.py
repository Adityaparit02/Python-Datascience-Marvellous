def table(n):
    a=list()

    for i in range(1, 11):
        mult=n*i
        a.append(mult)
    return print(list(a))

def main():
    num = int(input("Enter a number: "))
    table(num)

if __name__=="__main__":
    main()
