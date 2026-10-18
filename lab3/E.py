class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_front(self, n):
        self.items = [n] + self.items
        print("ok")

    def push_back(self, n):
        self.items.append(n)
        print("ok")

    def pop_front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop(0))

    def pop_back(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop())

    def front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[0])

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


dq = Deque()

while True:
    cmd = input().split()
    
    if cmd[0] == "push_front":
        dq.push_front(int(cmd[1])) 
    elif cmd[0] == "push_back":
        dq.push_back(int(cmd[1]))   
    elif cmd[0] == "pop_front":
        dq.pop_front()
    elif cmd[0] == "pop_back":
        dq.pop_back()
    elif cmd[0] == "front":
        dq.front()
    elif cmd[0] == "back":
        dq.back()
    elif cmd[0] == "size":
        dq.size()
    elif cmd[0] == "clear":
        dq.clear()
    elif cmd[0] == "exit":
        dq.exit()
        break