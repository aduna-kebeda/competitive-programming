# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr=[]
        def rec(root):
            if not root:
                return None
            
            if len(self.arr)>=k:
                return None
            rec(root.left)
            self.arr.append(root.val)
            rec(root.right)
        rec(root)
        print(self.arr)
        return self.arr[k-1]