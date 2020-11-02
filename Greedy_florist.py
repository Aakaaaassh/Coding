n,x = list(map(int,input().split()))
list1 = []
for i in range(n):
    y = int(input("enter price of flower"))
    list1.append(y)
print("number of flowers are " + str(n) + " and their prices are ", list1)
Buyer = x
print("Number of buyers are :", Buyer)
res = sorted(list1, reverse=True)
print(res)
def TotalPrice(res):
    count = 0
    price = 0
    k = 1
    for i in res:
        count += 1
        price = price + k*i
        if count == Buyer:
            k += 1
    return price
print(TotalPrice(res))

    








