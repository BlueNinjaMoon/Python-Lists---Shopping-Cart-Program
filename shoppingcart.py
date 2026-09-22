foodlist = []
pricelist = []
quantitylist = []

while True:
    food = input("Enter a food to buy (press Q to quit): ")
    if food.count("Q") == True or food.count("q") == True:
        break
    else:
        foodlist.append(food)
        price = input(f"How much does one {food} cost?: ")
        price = float(price)
        pricelist.append(price)
        quantity = input(f"How much {food}(s) do you want?: ")
        quantity = int(quantity)
        quantitylist.append(quantity)
    print(foodlist, pricelist, quantitylist)
    itemsubtotal = price * quantity
    itemsubtotallist = []
    subtotal = itemsubtotallist
    tax = subtotal * 0.006
    finaltotal = subtotal + tax