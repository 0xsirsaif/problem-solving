# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def _recur(node, raw=0, flag=True, left_order=0):
            if not node:
                return None, raw, flag, left_order

            if not node.right and not node.left:
                if flag:
                    return node.val, raw, flag, left_order
                return node.val, raw, flag, left_order

            left = _recur(node.left, raw+1, True, left_order)
            right = _recur(node.right, raw+1, False, left_order+1)

            print(left, right)
            if left[0] is None:
                return right
            elif right[0] is None:
                return left

            if not right[2]:
                return left
            elif not left[2]:
                return right
            else:
                if left[1] == right[1]:
                    return left if left[3] < right[3] else right
                else:
                    return left if left[1] > right[1] else right

        return _recur(root)[0]


n8 = TreeNode(3)
n7 = TreeNode(6, n8)
n6 = TreeNode(4)
n5 = TreeNode(2)
n4 = TreeNode(0)
n3 = TreeNode(5, n6, n7)
n2 = TreeNode(1, n4, n5)
n1 = TreeNode(3, n2, n3)

s = Solution()
print(s.findBottomLeftValue(n1))


# if left[1] and right[1]:
#     return left if (left[0] < right[0]) else right
# elif not left[1] and not right[1]:
#     return None, False
#
# return left if left[1] else right