def SieveOfEratosthenes(n):
    list1 = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        if list1[p] == True:

            for i in range(p*p,n+1,p):
                list1[i] = False
        p += 1
    
    for p in range(2,n+1):
        if list1[p]:
            print(p)

    for i in list1:
        if n == i:
            res = "Yes"
        else:
            res = "No"

    return list1, res
    


        



if __name__=='__main__': 
    n = int(input())
    print ("Following are the prime numbers smaller")
    print ("than or equal to", n )
    print(SieveOfEratosthenes(n)) 