import sys


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.search(key):
            return False
        self.root = self._add(self.root, key)
        return True
        
    def _add(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._add(node.left, key)
        elif key > node.data:
            node.right = self._add(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node

    def _print_tree(self, node, level):
        if node is None:
            return
        self._print_tree(node.left, level + 1)
        print("." * level + str(node.data))
        self._print_tree(node.right, level + 1)

    def print_tree(self):
        self._print_tree(self.root, 0)

tree = BinarySearchTree()
for line in sys.stdin:
    command = line.split()
    if not command:
        continue       
    if command[0] == "ADD":
        x = int(command[1])
        if tree.search(x):
            print("ALREADY")
        else:
            tree.add(int(x))
            print("DONE")
    elif command[0] == "DELETE":
        x = int(command[1])
        if tree.search(x):
            tree.delete(x)
            print("DONE")
        else:
            print("CANNOT")
    elif command[0] == "SEARCH":
        x = int(command[1])
        if tree.search(x):
            print("YES")
        else:
            print("NO")
    elif command[0] == "PRINTTREE":
        tree.print_tree()
    