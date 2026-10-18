from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
result = []

for i in range(N):
    if dq and dq[0] <= i - K:
        dq.popleft()
        
    while dq and arr[dq[-1]] >= arr[i]:
        dq.pop()
   
    dq.append(i)

    if i >= K - 1:
        result.append(arr[dq[0]])

for i in range(len(result)):
    print(result[i])