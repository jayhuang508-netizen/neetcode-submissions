class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        subset = []
        candidates.sort()
        

        def dfs(idx, target):
            if target == 0:
                res.add(tuple(subset.copy()))
            if target < 0 or idx >= len(candidates):
                return 
            
            subset.append(candidates[idx])
            dfs(idx+1, target-candidates[idx])
            subset.pop()

            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx+1, target)

        dfs(0, target)
        res = [list(s) for s in res]
        return res
