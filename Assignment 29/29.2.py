def ReadContents(FileName):
    try :
        fobj = open(FileName,"r")

        Data = fobj.read()
        print(Data)
        fobj.close()

    except FileNotFoundError as fobj:
        print("File Not found in Current Directory")

def main():
    FileName = input("Enter File Name :  ")
    ReadContents(FileName)
    
if __name__ == "__main__":
    main()
