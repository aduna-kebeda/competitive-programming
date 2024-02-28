# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rl(r):
            return [r.val]+rl(r.left)+rl(r.right) if r else [None]
        def rr(r):
            return [r.val]+rr(r.right)+rr(r.left) if r else [None]

        return rl(root.left)==rr(root.right) if root else True