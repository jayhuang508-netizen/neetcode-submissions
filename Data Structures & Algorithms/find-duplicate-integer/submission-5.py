class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linkedlist plus Floyd's 
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow] # slow continues to move
            slow2 = nums[slow2] # slow2 starts from beginning
            if slow == slow2:
                break
        return slow
                