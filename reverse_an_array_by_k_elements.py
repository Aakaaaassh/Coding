import math
n = int(input("Enter Size of Array: "))
k = int(input("k elements to be reversed: "))
a = list(map(int, input().strip().split()))[:n]
def ReverseInGroup(n,k,a):
    if len(a) <= k:
        return a[::-1]

    if len(a) > k:
        A = len(a)/k
        B = math.floor(float(len(a)/k))
        res = A-B
        list1 = []
        x = 0
        for i in range(B):
            x += k
            if x-k <= 0:
                temp = a[x-1::-1]
            else:
                temp = a[x-1:x-k-1:-1]
            list1.extend(temp)
            print(list1)
        if res > 0:
            temp = a[x:]
            res = temp[::-1]
            list1.extend(res)
    return list1       
print(ReverseInGroup(n,k,a))


    
