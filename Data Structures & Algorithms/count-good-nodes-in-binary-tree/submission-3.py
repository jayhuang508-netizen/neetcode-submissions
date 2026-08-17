# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 # at least the root
        path = [root.val]
        stack = [root] # first do dfs

        def dfs(node, path, res):
            if len(path)>0 and node.val >= path[-1]:
                res += 1
            appended = False
            # print(path)
            if node.left:
                appended = False
                if len(path) > 0 and node.left.val > path[-1]:
                     path.append(node.left.val)
                     appended = True
                res = dfs(node.left, path, res)
                if appended:
                    path.pop()  
            if node.right:
                appended = False
                if len(path) > 0 and node.right.val > path[-1]:
                     path.append(node.right.val)
                     appended = True
                res = dfs(node.right, path, res)
                if appended:
                    path.pop()
            return res
        res = dfs(root, path, res)
        return res