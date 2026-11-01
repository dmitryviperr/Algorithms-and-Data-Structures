import heapq


N = int(input())
cnt = 0
cargo = []

for i in range(N):
    l = list(map(int, input().split()))
    cargo.append(l)
cargo.sort(key=lambda x: x[0])

H  = []
heapq.heapify(H)

for s, t in cargo:
    end = s + t
    
    if H and H[0] <= s:
        heapq.heapreplace(H, end)
    else:
        heapq.heappush(H, end)
        cnt += 1

print(cnt)