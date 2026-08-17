# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base case：到底了，或找到了 p 或 q
        if root is None or root == p or root == q:
            return root

        # 在左右子树里分别找 p 和 q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 关键判断：
        if left and right:
            return root       # p、q 分别在两侧 → 当前节点就是 LCA
        return left or right
        