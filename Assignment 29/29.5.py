import sys

def ChkString(FileName,Stringx):
    fobj = open(FileName,"r")

    count = 0

    for lines in fobj:
        if lines == Stringx:
            count = count +1

        words = lines.split()

        for word in words:
            if word == Stringx:
                count = count +1
    fobj.close()
    return count

def main():
    FileName = sys.argv[1]
    Stringf = sys.argv[2]
    ret = ChkString(FileName,Stringf)

    print(f"The String {Stringf} is found {ret} times in {FileName}")

if __name__ =="__main__":
    main()