caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxyz"
while True:
    print("\nMAIN MENU")
    print("1) Encode a string")
    print("2) Decode a string")
    print("Q) Quit")
    ch=input("Enter your selection ==> ")
    if ch=='1':
        str1=input("Enter (brief) text to decrypt: ")
        shift=int(input("Enter the number to shift letters by: "))
        if shift>=1 and shift<=25:
            res=""
            for i in str1:
                if i.isupper():
                    res+=caps[(caps.index(i)+shift)%26]
                else:
                    res+=small[(small.index(i)+shift)%26]
            print("Decrypted: ",res)
    elif ch=='2':
        str1=input("Enter (brief) text to decrypt: ")
        shift=int(input("Enter the number to shift letters by: "))
        if shift>=1 and shift<=25:
            res=""
            for i in str1:
                if i.isupper():
                    res+=caps[(26+caps.index(i)-shift)%26]
                else:
                    res+=small[(26+small.index(i)-shift)%26]
            print("Decrypted: ",res)
    else:
        print("Caesar Thanks You!")
        break