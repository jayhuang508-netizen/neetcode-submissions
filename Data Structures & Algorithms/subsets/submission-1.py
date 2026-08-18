class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # i is the value of we are deciding on
        def dfs(i):
            if i >= len(nums):
                # the result is always the leaf node 
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
            


        