# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, minVal, maxVal) -> bool:
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False

            left = check(node.left, minVal, node.val)
            right = check(node.right, node.val, maxVal)
            return left and right
        return check(root, -float('inf'), float('inf'))
            