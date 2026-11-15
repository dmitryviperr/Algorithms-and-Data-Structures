from collections import deque
import sys


sys.setrecursionlimit(100000)

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

    def _balance(self, node):
        if node is None:
            return True

        left_tree = BinarySearchTree()
        left_tree.root = node.left
        
        right_tree = BinarySearchTree()
        right_tree.root = node.right

        if abs(left_tree._height() - right_tree._height()) > 1:
            return False

        return self._balance(node.left) and self._balance(node.right)

    def balance(self):
        return self._balance(self.root)
        

elems = list(map(int, input().split()))[:-1]

tree = BinarySearchTree()
for x in elems:
    tree.add(x)
if tree.balance():
    print("YES")
else:
    print("NO")