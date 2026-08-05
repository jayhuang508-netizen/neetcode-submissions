class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        m = (l+r)//2    
        while target != nums[m]:
            temp_m = m
            if target > nums[m]:
                l = m
                m = m + (r-m)//2
            elif target < nums[m]:
                r = m
                m = (m-l)//2
            if m+1 < len(nums) and target == nums[m+1]:
                return m+1
            if temp_m == m:
                return -1 # stuck
        return m
            



        