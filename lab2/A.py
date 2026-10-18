def bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] == x:
            return "YES"
        elif arr[m] < x:
            l = m          
        else:
            r = m          
    return "NO"


N, K = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

for i in range(K):
    print(bin_search(arr_1, arr_2[i]))