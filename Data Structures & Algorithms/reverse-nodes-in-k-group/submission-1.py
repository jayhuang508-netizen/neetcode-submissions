# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        # use extra k space, copy K, if works modify the link
        curr = head
        prev = dummy # find correct dummy is important

        # find the kth node
        def findKthNode(node, k):
            # return -1 if failed
            # return k+1 th node of node
            curr = node
            for i in range(k):
                if curr:
                    curr = curr.next
                else:
                    return -1
            return curr
            
        while curr:
            kth = findKthNode(curr, k)
            if kth == -1:
                return dummy.next

            for i in range(k):
                nxt = curr.next
                curr.next = kth
                kth = curr
                curr = nxt
            
            tmp = prev.next
            prev.next = kth
            prev = tmp

            
        return dummy.next






        
        
        