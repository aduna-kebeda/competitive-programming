# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    
        self._max  = -inf
        def rec(root,maxi,mini):
            if not root:
                return maxi-mini
            maxi = max(maxi, root.val)
            mini=min(mini, root.val)
            return max(rec(root.left,maxi,mini) ,rec(root.right,maxi,mini)  )         

        return rec(root, -inf ,inf )

       