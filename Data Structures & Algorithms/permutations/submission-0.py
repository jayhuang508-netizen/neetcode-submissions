class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                subset.append(nums[i])
                used[i] = True
                dfs()
                # when to cancel, remember to re-do everything
                subset.pop()
                used[i] = False
                

        dfs()
        return res

        