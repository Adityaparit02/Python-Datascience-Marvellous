class BankAccount():
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = int(Amount)

    def Display(self):
        print(f"Account Holder Name : {self.Name}")
        print(f"Current Balance : {self.Amount}")
        print()

    def Deposit(self):
        print(f"Current Balance : {self.Amount}")
        self.depositamt = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + self.depositamt
        print()

    def Withdraw(self):
        print(f"Current Balance : {self.Amount}")
        self.withdrawamt = int(input("Enter amount to withdraw : "))
        if self.Amount >= self.withdrawamt:
            self.Amount = self.Amount - self.withdrawamt
        else :
            print("Insufficient Balance")
        print()

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        return self.Interest
        print()
        print()
        print()

def main():
    obj1=BankAccount("Aditya",234000)
    print("#"*20 ,"Object 1", "*" * 20)
    print()
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    print(f"The Interest will be : {obj1.CalculateInterest()}")
    obj1.Display()

    print()

    print()
    
    print()
    print("#"*20 ,"Object 2", "*" * 20)
    print()
    obj2=BankAccount("Aditya","234000")
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    print(f"The Interest will be : {obj2.CalculateInterest()}")
    obj2.Display()

if __name__ == "__main__":
    main()