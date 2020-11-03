def NegativeElements(list):
    return sorted(list)

list = list(map(int, input().split()))
print(*NegativeElements(list))