class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            pair = target - n
            if i+1 > len(nums):
                return []
            if pair in set(nums[i+1:]):
                return [i, i+1+nums[i+1:].index(pair)]
        return []