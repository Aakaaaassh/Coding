n = int(input("Enter no. of test cases: "))
dict = {}
for i in range(n):
    a = int(input("Enter size of array: "))
    list1 = list(map(int, input().split()))
    res = sorted(list1)
    dict[i] = res
for key,values in dict.items():
    print(*values)