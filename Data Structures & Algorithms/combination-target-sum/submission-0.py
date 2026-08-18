class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i,  target):
            if target == 0:
                res.append(subset.copy())
                return
            if i >= len(nums) or target<0:
                return
            
            # try
            subset.append(nums[i])
            dfs(i, target-nums[i])
            subset.pop()
            
            # not try
            
            dfs(i+1,target)
            

        dfs(0, target)
        return res


        