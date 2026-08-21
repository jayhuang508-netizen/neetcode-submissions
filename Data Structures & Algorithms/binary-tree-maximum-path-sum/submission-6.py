# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        print(root.val)
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            righMax = max(right, 0)
            res = max(res, root.val + leftMax + righMax)
            # print(res)

            return root.val + max(leftMax, righMax)
        dfs(root)
        return res
        
        