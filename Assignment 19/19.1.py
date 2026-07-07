power=lambda n : n ** 2

def main():
    no=int(input("Enter Number: "))
    power_ret=power(no)
    print(f"Square of {no} is {power_ret}")

if __name__=="__main__":
    main()