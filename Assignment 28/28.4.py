def CopyContents(FileNameO,FileNameC):

    fobj1 = open(FileNameO,"r")
    fobj2 = open(FileNameC,"w")

    for lines in fobj1:
        fobj2.write(lines)

    fobj1.close()
    fobj2.close()

    print(f"Contents of {FileNameO} copied to {FileNameC}")

def main():
    FileName1 = input("Enter File Name to be copied : ")
    FileName2 = input("Enter File Name to copy to : ")

    CopyContents(FileName1,FileName2)

if __name__=="__main__":
    main()
