distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
d_sort = sorted(distances)
p_sort = sorted(prices, reverse=True)
sum = 0
for i in range(len(d_sort)):
    sum += d_sort[i] * p_sort[i]
print(sum)
