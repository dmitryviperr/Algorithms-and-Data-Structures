class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.count = 1


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
                current.count += 1
                return False
            
    def add(self, key):
        return self._add(key)

    def print_in_order(self):
        stack = []
        current = self.root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(f"{current.data} {current.count}")
            current = current.right


elems = list(map(int, input().split()))[:-1]

tree = BinarySearchTree()
for x in elems:
    tree.add(x)

tree.print_in_order()