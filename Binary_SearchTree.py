class Node:
    def __init__(self, key):
        self.left = None
        self.data = key
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(str(root.data) + " ", end="")
        inOrder(root.right)

def exists(node, val):
    if node is None:
        return False
    if val == node.data:
        return True
    if val < node.data:
        return exists(node.left, val)
    else:
        return exists(node.right, val)

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("InOrder:")
inOrder(root)
print()

x = int(input("Enter value you want to search: "))
if exists(root, x):
    print("Found")
else:
    print("Not Found")

