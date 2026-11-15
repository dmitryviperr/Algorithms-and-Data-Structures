class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _add(self, key):
        if self.root is None:
            self.root = Node(key)
            return True
        
        current = self.root
        while True:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    return True
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    return True
                current = current.right
            else:
                return False
            
    def add(self, key):
        return self._add(key)
    
    def _next(self, key):
        current = self.root
        x = -1
        while current is not None:
            if current.data >= key:
                x = current.data
                current = current.left  
            else:
                current = current.right
                
        return x
    def next(self, key):
        return self._next(key)

tree = BinarySearchTree()
last_answer = 0
has_query = False

n = int(input())
for _ in range(n):
    op, val = input().split()
    val = int(val)

    if op == '+':
        if has_query:
            val = (val + last_answer) % 10**9
        tree.add(val)
        has_query = False
    elif op == '?':
        last_answer = tree.next(val)
        print(last_answer)
        has_query = True
