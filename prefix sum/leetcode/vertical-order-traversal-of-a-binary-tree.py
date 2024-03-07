# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)

        def rec(root, row, col):
            if not root:
                return None
            dic[(row, col)].append(root.val)

            rec(root.left, row + 1, col - 1)
            rec(root.right, row + 1, col +1)
        rec(root, 0, 0)
        # print(dic)
        res=defaultdict(list)
        for key in sorted(dic.keys(),key=lambda x:x[0]):
            res[key[1]].extend(sorted(dic[key]))
       
        ans=[]
        for i in sorted(res.keys()):
            ans.append(res[i])
        return ans
