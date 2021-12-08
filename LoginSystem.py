username = 'Bob'

password = 'Bob'

userInput = input("Enter Your Username\n")

if userInput == username:
    a=input("Enter Your Password\n")
    if a == password:
        from menu import userwebhook
        
    else:
        print("That Password Is Incorrect!\n")
else:
    print("That Username Is Not Stored!\n")
