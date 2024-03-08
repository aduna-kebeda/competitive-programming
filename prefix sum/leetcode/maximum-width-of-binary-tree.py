# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(list)
        
        def rec(node, depth, position):
            if not node:
                return

            dic[depth].append(position)
            rec(node.left, depth + 1, 2 * position + 1)
            rec(node.right, depth + 1, 2 * position + 2)

        rec(root, 0, 1)
        maxi=0
        for key, val in dic.items():
            maxi=max(maxi, max(val)- min(val))
        return maxi + 1

    