class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        # dur to the negative, it always shifts between max and min
        for num in nums:
            tmp = curMax*num
            curMax = max(tmp, num*curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
        