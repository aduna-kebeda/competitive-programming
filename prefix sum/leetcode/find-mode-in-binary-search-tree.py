# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]

        def traverse(root):
            
            if not root :
                return None
            arr.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        cnt=Counter(arr)
        most=cnt.most_common()[0][1]
        ans=[]
        for key, val in cnt.items():
            if val==most:
                ans.append(key)
        return ans
            
        