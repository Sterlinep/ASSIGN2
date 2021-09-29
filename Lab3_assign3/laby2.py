print("Welcome to Flarsheim Guesser!")
choice ='y'
while(choice == 'Y' or choice == 'y'):
    print("\nPlease think of a number between and including 1 and 100.")
    Three_Remainder = 0
    Five_Remainder = 0
    Seven_Remainder = 0

    Three_Remainder = int(input("\nWhat is the remainder when your number is divided by 3 ?"))
    while (Three_Remainder < 0 or Three_Remainder >= 3):
        if Three_Remainder < 0:
            print("The value entered must be 0 or greater")
        elif Three_Remainder >= 3:
            print("The value entered must be less than 3")
        Three_Remainder = int(input("What is the remainder when your number is divided by 3 ?"))

    Five_Remainder = int(input("\nWhat is the remainder when your number is divided by 5 ?"))
    while (Five_Remainder < 0 or Five_Remainder >= 5):
        if Five_Remainder < 0:
            print("The value entered must be 0 or greater")
        elif Five_Remainder >= 5:
            print("The value entered must be less than 5")
        Five_Remainder = int(input("What is the remainder when your number is divided by 5 ?"))

    Seven_Remainder = int(input("\nWhat is the remainder when your number is divided by 7 ?"))
    while (Seven_Remainder < 0 or Seven_Remainder >= 7):
        if Seven_Remainder < 0:
            print("The value entered must be 0 or greater")
        elif Seven_Remainder >= 7:
            print("The value entered must be less than 7")

        Seven_Remainder = int(input("What is the remainder when your number is divided by 7 ?"))
    for i in range(1, 101):
        if (i % 3 == Three_Remainder and i % 5 == Five_Remainder and i % 7 == Seven_Remainder):
            print("Your number was", i)
            print("How amazing is that?\n")
    choice = input("Do you want to play again? Y to continue,N to quit ==>")
    while (choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n'):
        choice = input("Do you want to play again? Y to continue,N to quit ==>")