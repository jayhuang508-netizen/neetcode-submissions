class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        one, two = 0, 0
        for n in nums:
            temp = max(n+one, two)
            one = two
            two = temp
        return two
        