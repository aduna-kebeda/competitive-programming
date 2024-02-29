# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.arr=[]

        def rec(root):
            if not root:
                return None
            rec(root.left)
            self.arr.append(root.val)
            rec(root.right)
        rec(root)  
        return sorted(self.arr)==self.arr if len(set(self.arr))==len(self.arr) else False