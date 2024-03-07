# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(root, current_sum):
            if not root:
                return 0
            current_sum = current_sum * 10 + root.val
            if not root.left and not root.right:
                return current_sum
            return rec(root.left, current_sum) + rec(root.right, current_sum)

        total = rec(root, 0)
        return total
