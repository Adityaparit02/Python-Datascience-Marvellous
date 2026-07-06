import threading

def priteven():
    for i in range(2,22):
        if i%2==0:
            print(i,end=" ")

def main():
    t1=threading.Thread(target=priteven)
    t1.start()

if __name__=="__main__":
    main()