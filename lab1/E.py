def MergeSort(A):
    if len(A)  <= 1:
        return A
    ind = len(A) // 2
    left = MergeSort(A[:ind])
    right = MergeSort(A[ind:])
    return Merge(left, right)


def Merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])
    return res


N = int(input())
A = []

A = list(map(int, input().split())) 

A = MergeSort(A)
for x in A[:-1]:
    print(x, end=' ')
print(A[-1])