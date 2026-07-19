def CountWords(FileName):
    fobj = open(FileName,"r")

    count = 0
    for line in fobj:
        words = line.split()

        for word in words:
            count = count + 1

    fobj.close()
    return count

def main():
    FileName = "Demo.txt"
    ret = CountWords("Demo.txt")
    print(f"Number of Words in {FileName} are : {ret}")

if __name__=="__main__":
    main()