n = int(input("Enter size of array: "))
x = list(map(int, input().split()))
res = sorted(x, reverse=True)
print(res)