# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go through the list one to get the total number,
        # then delete the position at (length - n) th
        total_length = 0
        curr = head
        while curr != None:
            total_length += 1
            curr = curr.next
        target = total_length - n
        prev = ListNode()
        prev.next = head
        curr = head
        count = 0
        newhead = prev
        while curr != None:
            if count == target:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            count += 1
        return newhead.next

        