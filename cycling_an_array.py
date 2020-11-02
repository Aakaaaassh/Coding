n = int(input())
dict = {}
for i in range(n):
    a = int(input())
    b = list(map(int,input().split()))[:a]
    res1 = b[a-1]
    res2 = b[0:a-1]
    list2 = []
    list2.append(res1)
    for i in res2:
        list2.append(i)
    dict[i] = list2
for key,values in dict.items():
    print(*values)

