a = 9
b = 10
res = 0
list1 = []
n = int(input("Enter the value of n: "))
while res < n:
    list1.append(a)
    res = a * b
    a = a * b
list2 = list1
for i in list1[1:]:
    res = i
    for i in list1[0:]:
        if i < res:
            temp = res + i
            list2.append(temp)

print("Unsorted list is : " , list2)
print("Sorted List is: ",sorted(list2))


def SmallestNum(m):
    for i in list2:
        if i%m == 0:
            return i
result = []
t = int(input())
for i in range(t):
    m = int(input())
    res = SmallestNum(m)
    result.append(res)
for i in result:
    print(i)