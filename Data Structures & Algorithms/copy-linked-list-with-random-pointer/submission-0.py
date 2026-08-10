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
        # first go through the whole list, create the dictionary
        # second go through the original list to link the random 
        index_dict = {None: None} # node : node # default None point to None
        curr = head
        while curr != None:
            copy = Node(curr.val)
            index_dict[curr] = copy
            curr = curr.next
        
        curr = head
        while curr != None:
            copy = index_dict[curr]
            copy.next = index_dict[curr.next]
            copy.random = index_dict[curr.random]
            curr = curr.next
        return index_dict[head]

        