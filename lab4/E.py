import heapq


N = int(input())
H = list(map(int, input().split()))

heapq.heapify(H)
costs = 0

while len(H) > 1:
    left = heapq.heappop(H)
    right = heapq.heappop(H)
    s = left + right

    heapq.heappush(H, s)
    costs += s * 0.05

print(f"{costs:.2f}")