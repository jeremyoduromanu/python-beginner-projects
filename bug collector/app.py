def bug_counter():
    bug_collected = 0
    index = 1
    while index < 8:
        bugs_per_day = float(input("How many bugs did you collect on day " + str(index) + ": "))
        bug_collected = bug_collected + bugs_per_day
        index = index + 1
    print("You got " + str(int(bug_collected)) + " bugs in the week")

bug_counter() 
