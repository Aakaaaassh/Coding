n = int(input("Enter No. of test cases: "))
dict = {}
for k in range(n):
    a = list(map(int,input("Size of list1 and list2:").split()))
    list1 = list(map(int, input("Enter List1: ").split()))[:a[0]]
    list2 = list(map(int, input("Enter List2: ").split()))[:a[1]]
    list3 = []
    for i in list1:
        if i not in list3:
            list3.append(i)
    for j in list2:
        if j not in list3:
            list3.append(j)
    dict[k] = list3
for keys,values in dict.items():
    print(len(values), values)
        