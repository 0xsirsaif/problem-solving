class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution0:
    """
    brute force approach is to search for the target node in the original tree, and count nodes through traversing,
    then do the same traversing approach until reaches the target_count from prev traversing, there return cloned
    node
    ** not completed
    ** optimization is to traverse two tree in parallel until we reach the targeted node, there return cloned one
    (Solution2)
    """
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def pre_search(root: TreeNode, count, target_count=None):
            if not root:
                return 0
            print(root.val, target.val, count)
            if root == target:  # original tree
                return count
            if count == target:  # cloned tree
                return root
            left_sub_array = pre_search(root.left, count+1, target_count)
            if left_sub_array:
                return count
            right_sub_array = pre_search(root.right, left_sub_array+1, target_count)
            return right_sub_array

        return pre_search(cloned, 0, pre_search(original, 0, 0))


class Solution1:
    """
    This solution has to traverse all nodes and pack parallel nodes in the two tree together, then loop over tuple of
    nodes till reaches the targeted node in the original tree, there we return the cloned node (neighbour node)

    the non-generator-use approach is to traverse all nodes and store references in list, one list for each tree
    then zip(list,1, list2) and loop over them to find the target node

    What is the key benefit of using generator here?
    -> space wise , we don't have to initialize list and append nodes references
    """
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def _generator(node):
            if node:
                yield node
                yield from _generator(node.left)
                yield from _generator(node.right)

        for n1, n2 in zip(_generator(original), _generator(cloned)):
            if n1 == target:
                return n2


class Solution2:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        L = self.getTargetCopy(original.left, cloned.left, target)
        if L:
            return L
        return self.getTargetCopy(original.right, cloned.right, target)
