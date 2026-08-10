# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the second half -> two pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # revese the second half of list
        second = slow.next
        prev = slow.next = None
        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two list, now prev is the head of second half
        first, second = head, prev
        while second != None:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            

            
        
        