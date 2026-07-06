import threading

def displaylength(s):
    lengthx=len(s)
    print(lengthx)

def main():
    value=input("Enter string: ")
    t1=threading.Thread(target=displaylength,args=(value,))
    t1.start()

if __name__=="__main__":
    main()