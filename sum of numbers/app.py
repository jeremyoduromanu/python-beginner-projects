def sum_of_numbers():
    index = 1
    totalnum = 0
    while index > 0:
        usernum = float(input("Enter a number: "))
        if usernum > 0:
            totalnum = totalnum + usernum
        else:
            index =0
        
    print(totalnum)

sum_of_numbers()