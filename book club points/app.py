def customer_pts_check():
    num_of_purchased_books = float(input("How many books have you purchased: "))
    customer_pts = 0
    if num_of_purchased_books == 1:
        customer_pts = 5
    elif num_of_purchased_books == 2:
        customer_pts = 15
    elif num_of_purchased_books == 3:
        customer_pts = 30
    elif num_of_purchased_books == 4:
        customer_pts = 60
    else:
        customer_pts = (num_of_purchased_books * 15)
    print(str(customer_pts) + "pts")

customer_pts_check()
    
    
    

    