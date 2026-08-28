class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = [0] * n
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2,n):
            res[i] = max(res[i-2]+nums[i], res[i-1])
        return res[n-1]
        