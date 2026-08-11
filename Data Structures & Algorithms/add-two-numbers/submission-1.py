# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # when do the addition, consider whether there is a extra 1 from previous
        curr1 = l1
        curr2 = l2
        dummy = ListNode()
        curr_new = dummy

        add_one = False
        while curr1 and curr2:
            added_val = curr1.val + curr2.val
            # print(added_val)
            if add_one:
                # print(added_val)
                added_val += 1
                add_one = False
            new_val = 0
            if added_val >= 10:
                new_val = added_val - 10
                add_one = True
            else:
                new_val = added_val
            curr_new.next = ListNode(new_val)
            curr1 = curr1.next
            curr2 = curr2.next
            curr_new = curr_new.next

        while curr1:
            if add_one:
                curr1.val += 1
                add_one = False
            if curr1.val == 10:
                curr1.val = 0
                add_one = True
            curr_new.next = ListNode(curr1.val)
            curr1 = curr1.next
            curr_new = curr_new.next

        while curr2:
            if add_one:
                curr2.val += 1
                add_one = False
            if curr2.val == 10:
                curr2.val = 0
                add_one = True
            curr_new.next = ListNode(curr2.val)
            curr2 = curr2.next
            curr_new = curr_new.next
        
        if add_one:
            curr_new.next = ListNode(1)
        
        return dummy.next




            
