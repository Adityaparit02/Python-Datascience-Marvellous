import threading
def Marvellous():
    for i in range (5):
        print("Marvellous")

def main():
    t1=threading.Thread(target=Marvellous)
    t1.start()

if __name__=="__main__":
    main()