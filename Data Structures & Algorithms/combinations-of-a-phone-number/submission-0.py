class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [[], [], "abc", "def", "ghi", "jkl", "mno", "pqrs","tuv", "wxyz"]
        res = []
        subset = []
        if digits == "":
            return res

        def dfs(d):
            if  d == "":
                res.append(''.join(subset))
                return

            word = mapping[int(d[0])]
            for w in list(word):
                subset.append(w)
                dfs(d[1:])
                subset.pop()
        dfs(digits)
        return res

        