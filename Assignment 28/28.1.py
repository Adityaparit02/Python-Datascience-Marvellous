def CountLines(FileName):
    fobj = open("Demo.txt","r")

    count = 0

    for lines in fobj :
        count = count + 1

    fobj.close()
    return count

def main():
    FileName = "Demo.txt"
    ret = CountLines(FileName)

    print(f"Number of lines in {FileName} are {ret}" )

if __name__ =="__main__":
    main()