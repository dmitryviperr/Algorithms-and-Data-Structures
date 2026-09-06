from random import randint

def QuickSort(A, N):
    if N <= 1:
        return A
    val = A[randint(0, N - 1)]
    left = [elem for elem in A if elem < val]
    center = [elem for elem in A if elem == val]
    right = [elem for elem in A if elem > val]
    return QuickSort(left, len(left)) + center + QuickSort(right, len(right))

N = int(input())
A = []
while len(A) < N:
    for x in input().split():
        A.append(int(x))

A = QuickSort(A, N)
print(*A)  