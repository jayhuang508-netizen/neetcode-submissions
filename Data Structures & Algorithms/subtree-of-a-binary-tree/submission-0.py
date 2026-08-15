# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def compareTwoTree(self, q, p) -> bool:
        if q is None and p is not None:
            return False
        if q is not None and p is None:
            return False
        if q is None and p is None:
            return True
        return q.val == p.val and self.compareTwoTree(q.left, p.left) and self.compareTwoTree(q.right, p.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # first traverse the root tree, if find the vals of them are same
        # compare the tree
        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        res = False
        if root.val == subRoot.val:
                res = self.compareTwoTree(root, subRoot)
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        