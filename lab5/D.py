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
    
    def _second_largest(self, node):
        if node is None:
            return None

        parent = None
        current = node
        while current.right is not None:
            parent = current
            current = current.right

        if current.left is not None:
            left_node = current.left
            while left_node.right is not None:
                left_node = left_node.right
            return left_node.data

        if parent is not None:
            return parent.data

        return None

    def second_largest(self):
        return self._second_largest(self.root)


elems = list(map(int, input().split()[:-1]))

tree = BinarySearchTree()
for x in elems:
    tree.add(x)

print(tree.second_largest())

    

