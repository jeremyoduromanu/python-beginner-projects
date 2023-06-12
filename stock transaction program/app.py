
last_month = {
    "num_shares" : 1000,
    "price_pershare" : 32.87,
    "store_broker_commision" : 0.02 * (1000 * 32.87)
}

two_weeks = {
    "num_shares" : 1000,
    "price_pershare" : 33.92,
    "store_broker_commision" : 0.02 * (1000 * 33.92)
}

stock_purchased = last_month["num_shares"] * last_month["price_pershare"]
stock_sold = two_weeks["num_shares"] * two_weeks["price_pershare"]


print(last_month["num_shares"] * last_month["price_pershare"])
print(last_month["store_broker_commision"])
print(two_weeks["num_shares"] * two_weeks["price_pershare"])
print(two_weeks["store_broker_commision"])
print(stock_sold - (stock_purchased + last_month["store_broker_commision"] + two_weeks["store_broker_commision"]))