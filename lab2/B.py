def bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m       
        else:
            r = m   
    return l


N, K = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for i in range(K):
    pos = bin_search(arr_1, arr_2[i])
    if pos == -1:
        elem = arr_1[0]
    elif pos == N - 1:
        elem = arr_1[N-1]
    else:
        left = arr_1[pos]
        right = arr_1[pos + 1]
        if arr_2[i] - left <= right - arr_2[i]:
            elem = left
        else:
            elem = right
    print(elem)

