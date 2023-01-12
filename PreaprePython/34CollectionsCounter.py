def collectionsCounter(shoe_number, shoe_price, customer_number, shoe_size):
    total_money_earned = 0
    print("Show all keys", shoe_price.keys())

    for key in shoe_price.keys():
        if key in shoe_size:
            print("Shoe price: ", shoe_price[key])
            total_money_earned = total_money_earned + int(shoe_price[key])
    print(shoe_number)
    print(shoe_size)
    print(customer_number)
    print(shoe_price)
    return print("total: ", total_money_earned)

if __name__ == '__main__':
    shoe_number = int(input("Number of shoes: "))
    shoe_size = input("Available shoe sizes: ").split()
    customer_number = input("Number of customers: ")
    shoe_price = {}
    for i in range(int(customer_number)):
        j = input("Price per size: ").split()
        shoe_price[j[0]] = j[1]


    collectionsCounter(shoe_number, shoe_price, customer_number, shoe_size)