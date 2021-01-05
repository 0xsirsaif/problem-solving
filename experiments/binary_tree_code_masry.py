class BinaryTreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def length(self, node=None, longest_path=0):
        if not node:
            return longest_path
        left_sub_tree = self.length(node.left, longest_path+1)
        right_sub_tree = self.length(node.right, longest_path+1)
        longest_path = max(left_sub_tree, right_sub_tree)
        return longest_path


n3 = BinaryTreeNode(3)
n7 = BinaryTreeNode(8)
n6 = BinaryTreeNode(7)
n5 = BinaryTreeNode(5, n6, n7)
n4 = BinaryTreeNode(4)
n2 = BinaryTreeNode(2, n4, n5)
n1 = BinaryTreeNode(1, n2, n3)

BT = BinaryTree(n1)

print(BT.length(BT.root))
