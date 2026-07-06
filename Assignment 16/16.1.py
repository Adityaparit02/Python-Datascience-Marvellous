import threading

def fun():
    print("Hello from Fun")

def main():
    t1=threading.Thread(target=fun)
    t1.start()
    
if __name__=="__main__":
    main()