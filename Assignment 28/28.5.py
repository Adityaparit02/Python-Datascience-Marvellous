def WordSearch(FileName,WordX):
    fobj = open(FileName,"r")

    for lines in fobj:
        words = lines.split()

        for word in words:
            if word == WordX:
                print(f"Word Found in File {FileName}")
                fobj.close()
                return
            
    fobj.close()
    print("Word Not Found")


def main():
    FileName = input("Enter File Name : ")
    Word = input ("Enter Word to be searched : ")
    WordSearch(FileName,Word)

if __name__=="__main__":
    main()