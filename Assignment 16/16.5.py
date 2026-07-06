import threading

def printnos():
    for i in range (11):
        print(i,end="  ")

def main():
    t1=threading.Thread(target=printnos)
    t1.start()

if __name__=="__main__":
    main()