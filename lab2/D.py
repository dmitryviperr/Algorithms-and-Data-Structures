def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


a, b, c, d = map(int, input().split())
left = -1e5
right = 1e5  

for _ in range(100):
    mid = (left + right) / 2
    if f(mid, a, b, c, d) < 0 and f(left, a, b, c, d) < 0 or f(mid, a, b, c, d) >= 0 and f(left, a, b, c, d) >= 0:
        left = mid
    else:
        right = mid
    
print(f"{(left + right) / 2:.4f}")


