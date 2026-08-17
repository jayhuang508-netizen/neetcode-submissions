# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findPath(root, target, path):
            if root is None:
                return False
            path.append(root)
            if root == target:
                return True
            if findPath(root.left, target, path) or findPath(root.right, target, path):
                return True
            path.pop()
            return False
        
        path_p, path_q = [], []
        findPath(root, p, path_p)
        findPath(root, q, path_q)

        lca = None
        for a, b in zip(path_p, path_q):
            if a == b:
                lca = a
        return lca



        