# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # because the result is in level order 
        # so use the queue
        if root is None:
            return []
        res = []
        queue = deque([root])
        while len(queue)>0:
            # print([q.val for q in queue])
            # for each level, only append the last value
            n = len(queue)
            for i in range(n):
                if i == n - 1:
                    res.append(queue[0].val)
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # the last one of this level 
                
                    
        return res



        