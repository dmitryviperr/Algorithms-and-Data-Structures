stack = []
expr = input().split()

for elem in expr:
    if elem.isdigit():
        stack.append(int(elem))
    elif elem in ['+', '-', '*']:
        right = stack.pop()
        left = stack.pop()
        if elem == '+':
            res = left + right
        elif elem == '-':
            res = left - right
        elif elem == '*':
            res = left * right
        stack.append(res)
print(stack[0])
