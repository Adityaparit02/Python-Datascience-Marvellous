#seek(kuthe,kuthun)
#kuthun(0,1,2):
#0 - start
#1 - current
#2 - end

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")

        fobj.seek(10,0)
        Data = fobj.read()
        print(Data)
    except FileNotFoundError as fobj:
        print("file is not present in current directory")
        
if __name__ == "__main__":
    main()