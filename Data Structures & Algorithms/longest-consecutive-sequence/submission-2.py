class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums_set = set(nums)
        longest = 1
        for n in nums_set:
            if n-1 not in nums_set: # floor number
                temp_streak = 1
                j = n + 1
                while j in nums_set:
                    temp_streak += 1
                    longest = max(longest,temp_streak)
                    j += 1
            
        return longest
        
                


        