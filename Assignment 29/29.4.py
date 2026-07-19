import sys

def ChkContents(FileName1,FileName2):
    fobj1 = open(FileName1,"r")
    fobj2 = open(FileName2,"r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    if Data1 ==  Data2:
        print("Success")

    else:
        print("Failure")

    fobj1.close()
    fobj2.close()
    return

def main():
    Fileo = sys.argv[1]
    FileC = sys.argv[2]

    ChkContents(Fileo,FileC)

if __name__ =="__main__":
    main()

