class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        subset = []

        def dfs(i):
            res.add(tuple(subset[:]))
            if i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return [list(s) for s in res]

        