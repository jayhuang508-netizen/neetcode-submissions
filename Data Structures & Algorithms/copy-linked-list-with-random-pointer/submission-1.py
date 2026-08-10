"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        index_dict = collections.defaultdict(lambda: Node(0))
        index_dict[None] = None

        curr = head
        while curr != None:
            index_dict[curr].val = curr.val
            index_dict[curr].next = index_dict[curr.next]
            index_dict[curr].random = index_dict[curr.random]
            curr = curr.next
        return index_dict[head]

        