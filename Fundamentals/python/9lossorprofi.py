#here is question we need to take input from user of cost price and selling 
#price and show that profit or loss
cost_price = int(input("entre the cost price: "))
sell_price = int(input("entre the sell price: "))

if sell_price > cost_price:
    profit = sell_price - cost_price
    print("we have made a profit of ",profit)
    
elif sell_price < cost_price:
    loss = cost_price - sell_price
    print("we have loss the amount by ",loss)

#if sp==cp then no profit no loss
else:
    print("no profit no loss")
