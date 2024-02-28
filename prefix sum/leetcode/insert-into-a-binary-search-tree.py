# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       
        def insert(root, val):
            if not root:
               return TreeNode(val)
            if val < root.val:
                root.left=insert(root.left, val)
                return root 
            if val > root.val:
                root.right=insert(root.right, val)
                return root 
        return insert(root, val)
       
       
       
       
        # temp = root
        # temp2=temp
        # while temp:
        #     temp2=temp
        #     if val < temp.val:
        #         temp=temp.left
                
        #     elif val > temp.val:
        #         temp = temp.right
        #     else
            

