# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # the diff of left and right is less than 1
        if not root:
            return True
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

