import sys

def main():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print ("Please execute the script as ")
            print("python3 FileName.py DirectoryName")
            print("Directory Name should be absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is : ",DirectoryName)

    else:
        print("Invalid Number of arguments")
        print("Please use --h or --u for more information")


if __name__ =="__main__":
    main()