class Queue:
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
            print(self.items.pop(0))

    def front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[0])  

    def size(self):
        print(len(self.items))     

    def clear(self):
        self.items.clear()
        print("ok")

    def exit(self):
        print("bye")


q = Queue()

while True:
    cmd = input().split()
    
    if cmd[0] == "push":
        q.push(int(cmd[1]))    
    elif cmd[0] == "pop":
        q.pop()
    elif cmd[0] == "front":
        q.front()
    elif cmd[0] == "size":
        q.size()
    elif cmd[0] == "clear":
        q.clear()
    elif cmd[0] == "exit":
        q.exit()
        break