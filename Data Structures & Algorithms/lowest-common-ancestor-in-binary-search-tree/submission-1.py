# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = {root: None}
        stack = [root]
        # find until two nodes are all seen
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left) 
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        # find all ancestors of p
        ancesstors = set()
        while p:
            ancesstors.add(p)
            p = parents[p]
        
        while q:
            if q in ancesstors:
                return q
            q = parents[q]
        return root
        