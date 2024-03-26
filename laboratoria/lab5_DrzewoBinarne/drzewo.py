# Filip Połatyński

class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


def min_key(temp):
    ptr = temp
    while ptr.left and ptr.left.left:
        ptr = ptr.left
    if ptr.left:
        return ptr.left, ptr
    else :
        return ptr,


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, key):
        return self.__search(key, self.root)

    def __search(self, key, node):
        # If tree ends
        if not node:
            return None
        # If key found return val
        if key == node.key:
            return node.val
        # If key is bigger then node search right side of a tree
        elif key > node.key:
            return self.__search(key, node.right)
        # if key is smaller search left side of the tree
        elif key < node.key:
            return self.__search(key, node.left)
        else:
            return None

    def insert(self, key, val, node="start"):
        # Start from root
        if node == "start":
            node = self.root
        # If root is None
        if node is None:
            self.root = Node(key, val)
        # If found node
        elif key == node.key:
            node.val = val
        # If key is bigger then node search right side of a tree
        elif key > node.key:
            # If node exist search more, else insert new Node
            if node.right:
                self.insert(key, val, node.right)
            else:
                node.right = Node(key, val)
        # If key is smaller then node search right side of a tree
        elif key < node.key:
            # If node exist search more, else insert new Node
            if node.left:
                self.insert(key, val, node.left)
            else:
                node.left = Node(key, val)

    def delete(self, key, node="start", parent=None):
        # Start from root
        if node == "start":
            node = self.root
        if node is None:
            pass
        # Key does not exists
        elif key is None:
            print("Key does not exist")
        # If found perform deletion
        elif key == node.key:
            # REMOVAL
            # for node without children remove node
            if node.left is None and node.right is None:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            # for node with 2 childrens
            elif node.left and node.right:
                m = min_key(node.right)
                node.val = m[0].val
                node.key = m[0].key
                if len(m) > 1:
                    m[1].left = None
                else:
                    node.right = m[0].right
            # for node with one children
            else:
                if node.left is None:
                    if parent.right is node:
                        parent.right = node.right
                    else:
                        parent.left = node.right
                else:
                    if parent.right is node:
                        parent.right = node.left
                    else:
                        parent.left = node.left


        # If key is bigger then node search right side of a tree
        elif key > node.key:
            self.delete(key, node.right, node)
        # if key is smaller search left side of the tree
        elif key < node.key:
            self.delete(key, node.left, node)

    def heights(self):
        return self.__height(self.root, 0)

    def __height(self, node, suma=0):
        if node is None:
            return suma
        return max(self.__height(node.right, suma + 1), self.__height(node.left, suma + 1))

    def __print(self, node):
        if node.left is None and node.right is None:
            return [f"{node.key}: {node.val}"]
        else:
            if node.left and node.right:
                return self.__print(node.left) + [f"{node.key}: {node.val}"] + self.__print(node.right)
            elif node.left:
                return self.__print(node.left) + [f"{node.key}: {node.val}"]
            else:
                return [f"{node.key}: {node.val}"] + self.__print(node.right)

    def print(self):
        print("[" + ", ".join(self.__print(self.root)) + "]")

    def min_key(self):
        ptr = self.root
        while ptr.left:
            ptr = ptr.left
        return ptr

    def print_tree(self):
        print("=======================")
        self.__print_tree(self.root, 0)
        print("=======================")

    def __print_tree(self, node, lvl):
        if node == "start":
            node = self.root
        if node is not None:
            self.__print_tree(node.right,lvl+5)
            print()
            print(lvl*" ", node.key, node.val )

            self.__print_tree(node.left, lvl+5)


def main():
    BST = BinaryTree()
    d = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, val in d.items():
        BST.insert(key, val)
    BST.print_tree()
    BST.print()
    print(BST.search(24))
    BST.insert(6, "M")
    BST.delete(62)
    BST.insert(59, "N")
    BST.insert(100, "P")
    BST.delete(8)
    BST.delete(15)
    BST.insert(55, "R")
    BST.delete(50)
    BST.delete(5)
    BST.delete(24)
    BST.heights()
    BST.print()
    BST.print_tree()


main()
