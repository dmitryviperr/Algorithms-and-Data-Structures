import math

C = float(input())

left = 0.0
right = 1e5  

for _ in range(100):
    mid = (left + right) / 2
    if mid ** 2 + math.sqrt(mid) < C:
        left = mid
    else:
        right = mid

print(f"{left:.9f}")