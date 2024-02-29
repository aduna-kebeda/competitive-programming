# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic=defaultdict(list)
        def rec(root, idx):
            if not root:
                return None
            self.dic[idx].append(root.val)
            rec(root.left, idx + 1)
            rec(root.right, idx + 1)
        
        idx=0
        rec(root, idx)
        arr=[]
        for key, lst in self.dic.items():
            if key%2:
                arr.append(lst[::-1])
            else:
                 arr.append(lst)
        return arr
             

      
            
      
