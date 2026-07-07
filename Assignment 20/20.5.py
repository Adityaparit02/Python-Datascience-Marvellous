import threading

def printnos(n):
    for i in range (1,n+1):
        print(i,end="  ")
    print()

def printnos_rev(n):
    for i in range (n,0,-1):
        print(i, end="  ")
    print()
    
def main():
    t1=threading.Thread(target=printnos ,args=(50,))
    t2=threading.Thread(target=printnos_rev ,args=(50,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()