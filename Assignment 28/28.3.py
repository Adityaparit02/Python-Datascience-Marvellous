def DisplayLines(FileName):

    fobj = open(FileName,"r")

    for lines in fobj:
        print(lines)
        print("-------")

    fobj.close()

def main():
    FileName = "Demo.txt"
    DisplayLines(FileName)

if __name__=="__main__":
    main()