import heapq

n = int(input())
sizes = []
for _ in range(n):
    sizes.append(int(input()))


heap = []
for i in range(n):
    first_time = max(1000 - sizes[i], 1)
    heapq.heappush(heap, (first_time, i))

cur_time = 0
pos = 0  

while heap:
    t, idx = heapq.heappop(heap)
    travel = abs(pos - idx)

    if cur_time + travel > t:
        print(t)
        break

    cur_time = t
    pos = idx

    sizes[idx] += 1

    next_interval = max(1000 - sizes[idx], 1)
    next_time = t + next_interval
    
    heapq.heappush(heap, (next_time, idx))