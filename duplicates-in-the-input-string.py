n = list(map(str,input().strip().split()))
list1 = []
for i in n:
    if i not in list1:
        list1.append(i)
for i in list1:
    if n.count(i) > 1:
        print(i,n.count(i))