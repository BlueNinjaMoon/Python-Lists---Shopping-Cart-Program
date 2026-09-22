foodlist = []
pricelist = []
quantitylist = []
finaltotallist = []
taxlist = []
itemsubtotallist = []
maxindex = -1
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
    maxindex += 1
    itemsubtotal = price * quantity
    itemsubtotallist.append(itemsubtotal)
    tax = itemsubtotal * 0.006
    taxlist.append(tax)
    finaltotal = itemsubtotal + tax
    finaltotallist.append(finaltotal)
if maxindex == -1:
    print("Nothing was ordered.")
else:
    print("--------------- RECEIPT ---------------")
    while maxindex > -1:
            print(f"{foodlist[maxindex]}")
            print(f"Price: {pricelist[maxindex]}")
            print(f"Quantity: {quantitylist[maxindex]}")
            print(f"Item Subtotal: {itemsubtotallist[maxindex]}")
            print("")
            maxindex -= 1
            finaltotal1 = finaltotallist[maxindex] + finaltotallist[maxindex-1]
            tax1 = taxlist[maxindex] + taxlist[maxindex-1]
            subtotal1 = itemsubtotallist[maxindex] + itemsubtotallist[maxindex-1]
    print("---------------------------------------")
    print(f"Subtotal: {subtotal1:.2f}")
    print(f"Tax (6%): {tax1:.2f}")
    print(f"Total: {finaltotal1:.2f}")
    print("---------------------------------------")