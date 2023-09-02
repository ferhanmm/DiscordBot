#setting up how much is in my wallet
wallet = [ 1, 1, 1, 1, 1 ]

#creating a variable to store how much I spend
moneySpent = 0

#use each bill in the wallet
for bill in wallet:

    print("I'm holding the $" + str(bill) + " bill.")

    print("Putting $" + str(bill) + " in vending machine.")
          
    moneySpent += bill

    print("You have spent $" + str(moneySpent))
