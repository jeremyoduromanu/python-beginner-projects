def land_calc():
    square_feet = float(input("Enter the total square feet of the land: "))
    to_acres = square_feet / 43560
    print("Your land in square feet is " + str(to_acres))

land_calc()