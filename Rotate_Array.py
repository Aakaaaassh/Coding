def rotateArr(A,D,N):
    return A[D:] + A[:D]
A = list(map(int,input().strip().split()))
D = int(input())
N = len(A)
print(rotateArr(A,D,N))