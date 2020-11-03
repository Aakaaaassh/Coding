n = int(input("Enter the range: "))
list2 = []
total = 1
for i in range(2,n+1):
    res = i
    if total%res == 0:
        continue
    else:
        while res*i <= n:
            res = res*i
        total  *= res
    list2.append(res)
lcm = 1
for i in list2:
    lcm *= i
print(lcm)

    

