count = int(input())
dct = {}

for i in range(count):
    lst = input().split()
    product = lst[0]
    qty = int(lst[1])
    dct[product] = qty

count2 = int(input())

for j in range(count2):
    lst2 = input().split()
    action = lst2[0]
    prod = lst2[1]
    amount = int(lst[2])
    
    if action == "SELL":
        if dct[product] >= amount:
            dct[product] -= amount
        else:
            print("Insufficient stock:", product)
    elif action == "ADD":
        if product in dct:
            dct[product] += amount
        else:
            dct[product] = amount

for product in dct:
    print(product, dct[product])