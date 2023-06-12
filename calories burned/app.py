minutes = [10,15,20,25,30]
calories_per_min = 3.9

def calories_calc():
    calories_burned = 0
    index = 0
    while index < 5:
        minute_now = minutes[index]
        calories_burned = minutes[index] * calories_per_min
        minute_now = minutes[index]
        print(str(calories_burned) + " is burned after " + str(minute_now) + "mins")
        index = index + 1
        
        

calories_calc()
