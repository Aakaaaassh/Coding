str1 = input()
str2 = input()
def Checker(str1,str2):
    if len(str1) != len(str2):
        return -1
    if len(str1) == len(str2):
        temp = str1 + str1
        if str2 in temp:
            return True
        else:
            return False
print(Checker(str1,str2))