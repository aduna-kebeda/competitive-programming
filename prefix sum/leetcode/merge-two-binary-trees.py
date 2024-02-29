# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(root1, root2):
            
            if not root1 and not root2:
                return None
            elif root1 and not root2:
               return root1
            elif root2 and not root1:
               return root2
            elif root1 and root2:
                x = root1.val + root2.val 
                root1.val = x
                root1.left = rec(root1.left, root2.left)
                root1.right = rec(root1.right, root2.right)
                return root1
            print(root1)
        return rec(root1, root2)
        