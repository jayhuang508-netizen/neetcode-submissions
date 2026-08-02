class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            pair = target - n
            if i+1 > len(nums):
                return []
            if pair in set(nums[i+1:]):
                for j, m in enumerate(nums[i+1:]):
                    if m == pair:
                        return [i,j+i+1]
        return []