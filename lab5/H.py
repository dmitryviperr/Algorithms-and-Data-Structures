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
    
    def _branches(self, node):
        if node is None:
            return 
        self._branches(node.left)
        if node.left and node.right is None or node.right and node.left is None:
            print(node.data, end = '\n')
        self._branches(node.right)

    def branches(self):
        self._branches(self.root)
        

elems = list(map(int, input().split()))[:-1]

tree = BinarySearchTree()
for x in elems:
    tree.add(x)
tree.branches()