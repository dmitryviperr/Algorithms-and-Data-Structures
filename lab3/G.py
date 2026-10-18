n = int(input())

train = list(map(int, input().split()))

dead_end = []

expected = 1

for wagon in train:
    dead_end.append(wagon)

    while dead_end and dead_end[-1] == expected:
        dead_end.pop()
        expected += 1

if expected == n + 1:
    print("YES")
else:
    print("NO")