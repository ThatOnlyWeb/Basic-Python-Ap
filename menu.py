print("\nWelcome to the menu section")
print("What program do you want to open?\nyour options are:\nCalculator,Computer Crasher\nYou can also type Credits too see the credits :)")
Userinp = input()
if Userinp == "Calculator":
    from CalculatorFile import Calculatex
    
elif Userinp == "Computer Crasher":
    from CrasherScript import Crasherx

elif Userinp == "Credits":
    from Credits import CreditsVar
