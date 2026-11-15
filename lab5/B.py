from collections import deque

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
            return

        current = self.root
        while True:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    break
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    break
                current = current.right
            else:
                break

    def add(self, key):
        return self._add(key)

    def _height(self):
        if self.root is None:
            return 0
            
        q = deque([self.root])
        levels = 0
        
        while q:
            level_size = len(q)
            levels += 1
            
            for _ in range(level_size):
                current_node = q.popleft()
                if current_node.left is not None:
                    q.append(current_node.left)
                if current_node.right is not None:
                    q.append(current_node.right)
                    
        return levels
    
    def height(self):
        return self._height()

elems = list(map(int, input().split()[:-1]))

tree = BinarySearchTree()
for x in elems:
    tree.add(x)

print(tree.height())