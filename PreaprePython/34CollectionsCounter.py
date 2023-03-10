from collections import Counter

def collectionsCounter(shoe_number, shoe_price, customer_number, shoe_size):
    available_shoes = Counter(shoe_size)
    total_price = 0

    for i in shoe_price:
        if i[0] in available_shoes.keys():
            if available_shoes[i[0]] >=1:
                available_shoes[i[0]] = available_shoes[i[0]] - 1
                total_price = total_price + int(i[1])
    return total_price


if __name__ == '__main__':
    shoe_number = int(input())
    shoe_size = input().split()
    customer_number = input()
    shoe_price = []
    for i in range(int(customer_number)):
        j = input().split()
        shoe_price.append((j[0],j[1]))


    print(collectionsCounter(shoe_number, shoe_price, customer_number, shoe_size))