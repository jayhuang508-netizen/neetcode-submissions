class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for n in nums:
            unique_set.add(n)
        if len(nums) > len(unique_set):
            return True
        else:
            return False
            