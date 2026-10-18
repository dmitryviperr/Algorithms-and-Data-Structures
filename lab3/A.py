class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, n):
        self.items.append(n)
        print("ok")

    def pop(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop())

    def back(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[-1])  

    def size(self):
        print(len(self.items))     

    def clear(self):
        self.items.clear()
        print("ok")

    def exit(self):
        print("bye")


stack = Stack()

while True:
    cmd = input().split()
    
    if cmd[0] == "push":
        stack.push(int(cmd[1]))    
    elif cmd[0] == "pop":
        stack.pop()
    elif cmd[0] == "back":
        stack.back()
    elif cmd[0] == "size":
        stack.size()
    elif cmd[0] == "clear":
        stack.clear()
    elif cmd[0] == "exit":
        stack.exit()
        break