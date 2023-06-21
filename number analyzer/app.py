def numberAnalyzer():
    userNum = input("Enter an integer: ")
    if int(userNum) == 0:
        print("Your number is equal to zero")
    elif int(userNum) > 0:
        print("Your number is positive")
    else:
        print("Your number is negative")

numberAnalyzer()