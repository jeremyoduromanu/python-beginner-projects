def color_mixer():
    first_color = input("What is your first primary color: ")
    second_color = input("What is your second primary color: ")
    if (first_color == "red" or first_color == "blue") and (second_color == "blue" or second_color == "red"):
        print("You created color Purple")
    elif (first_color == "red" or first_color == "yellow") and (second_color == "yellow" or "red"):
        print("You created color orange")
    elif (first_color == "blue" or first_color == "yellow") and (second_color == "yellow" or "blue"):
        print("You created color green")
    else:
        print("The color you entered is not a primary color")

color_mixer()