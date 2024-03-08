# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def rec(root):
            if not root:
                return None
            
            rec(root.left)
            arr.append(root.val)
            rec(root.right)

        rec(root)

        def construct(left, right):
            if left>right:
                return 
            mid=(left + right)//2
            
            left=construct(left, mid -1)
            right=construct(mid + 1, right)
            head=TreeNode(arr[mid], left, right)

            return head
        return construct(0, len(arr)-1)
        

        