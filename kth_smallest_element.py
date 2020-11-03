n = int(input("Enter no. of test cases: "))
list2 = []
for i in range(n):
    a = int(input("Enter size of array: "))
    list1 = list(map(int, input().split()))
    k = int(input("Enter kth smallest element: "))
    res = sorted(list1)
    res = res[k-1]
    list2.append(res)
for i in list2:
    print(i)
