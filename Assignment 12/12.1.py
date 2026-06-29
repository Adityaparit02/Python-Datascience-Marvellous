from Library_12 import VowelCheck

def main():
    a=input("Enter the Character: ")
    b=VowelCheck(a)
    if VowelCheck(a):
        print (" Is a vowel")
    else:
        print ("Is not a vowel")

if __name__=="__main__":
    main()