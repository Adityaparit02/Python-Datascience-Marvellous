import sys

def CopyContents(FileName1,FileName2):

    fobj1 = open(FileName1,"r")
    fobj2 = open(FileName2,"w")

    for lines in fobj1:
        fobj2.write(lines)

    fobj1.close()
    fobj2.close()
    print(f"File Named {FileName1} copied to {FileName2}")

def main():
    FileNameo = sys.argv[1]
    FileNameC = sys.argv[2]

    CopyContents(FileNameo,FileNameC)

if __name__ =="__main__":
    main()
     
