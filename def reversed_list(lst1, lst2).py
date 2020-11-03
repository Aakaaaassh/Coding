def reversed_list(lst1, lst2):
  rev_list = []
  rev = 0
  while len(lst2) > 0:
      for i in lst2:
        rev = lst2.pop()
        rev_list.append(rev)
  if lst1 == rev_list:
    return True
  else:
    return False


list1 = list(map(int,input().strip().split()))
list2 = list(map(int,input().strip().split()))
#Uncomment the lines below when your function is done
print(reversed_list(list1,list2))
