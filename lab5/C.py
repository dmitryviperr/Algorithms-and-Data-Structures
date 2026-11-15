class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _add(self, key):
        if self.root is None:
            self.root = Node(key)
            self.size += 1
            return
        
        current = self.root
        while True:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    self.size += 1
                    break
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    self.size += 1
                    break
                current = current.right
            else:
                break
    def add(self, key):
        return self._add(key)

    def _count_elements(self):
        return self.size

    def count_elements(self):
        return self._count_elements()

elems = list(map(int, input().split()[:-1]))

tree = BinarySearchTree()
for x in elems:
    tree.add(x)

print(tree.count_elements())