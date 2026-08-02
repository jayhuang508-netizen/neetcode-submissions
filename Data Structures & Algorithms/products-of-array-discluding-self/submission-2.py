class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        sufix = [1 for _ in range(len(nums))]
        # first contruct prefix
        for i,n in enumerate(nums):
            if i ==0:
                prefix[i] = prefix[i]*n
            else:
                prefix[i] = prefix[i-1]*n
        # second construct sufix
        for j in range(len(nums)-1,-1,-1):
            if j+1 == len(nums):
                sufix[j] = sufix[j] * nums[j]
            else:
                sufix[j] = sufix[j+1] * nums[j]
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                res[i] = sufix[i+1]
            elif i == len(nums)-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * sufix[i+1]
        return res
        