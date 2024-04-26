class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_null_subtrees(node):
    if node is None:
        return 1
    return count_null_subtrees(node.left) + count_null_subtrees(node.right)

# Creating our tree
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(7)
root.right.right.right = Node(9)

# The number of null subtrees is its n nodes + 1
print(count_null_subtrees(root))
