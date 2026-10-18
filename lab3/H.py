from collections import deque


n = int(input())

left = deque()
right = deque()

result = []

for _ in range(n):
    line = input().split()
    cmd = line[0]
    
    if cmd == '+':
        right.append(line[1])
        
    elif cmd == '*':
        right.appendleft(line[1])
        
    elif cmd == '-':
        result.append(left.popleft())
        
    if len(left) < len(right):
        left.append(right.popleft())
        
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())

for i in range(len(result)):
    print(result[i])