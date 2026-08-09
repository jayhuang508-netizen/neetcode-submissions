# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one = two = head
        while two != None and two.next != None and two.next.next != None:
            two = two.next.next
            one = one.next
            if one.val == two.val:
                return True
        return False


        