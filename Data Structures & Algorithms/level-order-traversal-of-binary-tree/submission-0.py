# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # because it needs the value from left to right
        # so it uses the queue
        if root is None:
            return []
        queue = deque([root])
        result = [[root.val]]
        while len(queue) > 0:
            level_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level_res.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    level_res.append(node.right.val)
            if len(level_res) > 0:
                result.append(level_res)
        return result


        