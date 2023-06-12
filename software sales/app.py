num_of_purchased = float(input("How many packages did you purchased: "))

def calculate_discount():
    discount = 0
    if num_of_purchased < 10:
        print("You have to purchase more than 10")
    elif num_of_purchased in range(10,19):
        discount = 0.20 * num_of_purchased
    elif num_of_purchased in range(20,49):
        discount = 0.30 * num_of_purchased
    elif num_of_purchased in range(50,99):
        discount = 0.40 * num_of_purchased
    elif num_of_purchased >= 100:
        discount = 0.5 * num_of_purchased
    else:
        print("Enter a valid number")
    return discount
    


print("Your discount is $" + str(calculate_discount()))