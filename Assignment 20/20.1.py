import threading

def even_display(n):
    arr=list()
    for i in range(2,n+10):
        if i % 2== 0:
            arr.append(i)

    print (list(arr))


def odd_display(n):
    arr=list()
    for i in range(1,n+10):
        if i % 2 != 0:
            arr.append(i)

    print (list(arr))

def main():
    t1=threading.Thread(target=even_display,args=(10,))
    t2=threading.Thread(target=odd_display,args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()