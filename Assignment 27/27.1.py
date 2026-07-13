class BookStore():
    NoOfBooks = 0
    instance_count = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.instance_count = BookStore.instance_count+1
    
    def Display(self):
        print(f"{self.Name} by {self.Author} . No of books : {BookStore.instance_count}")

def main():
    obj1 = BookStore("Linux System Programming" , "Robert Love")
    obj1.Display()

    obj1 = BookStore("C Programming" , "Dennis Ritchie")
    obj1.Display()

if __name__ == "__main__":
    main()