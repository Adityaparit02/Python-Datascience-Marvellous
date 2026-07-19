import os 

def CheckExists(FileName):

    if (os.path.exists(FileName)):
        print("File is present in current Directory")

    else:
        print("There is no such File")

def main():

    FileName = input("Enter Name of File : ")
    CheckExists(FileName)
    

        
if __name__ == "__main__":
    main()