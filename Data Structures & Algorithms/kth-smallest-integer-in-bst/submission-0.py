# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # mid-order traverse and return k-1th position
        res = []
        def midOrder(node):
            if not node:
                return
            midOrder(node.left)
            res.append(node.val)
            midOrder(node.right)
        midOrder(root) 
        # print(res)
        return res[k-1]

        