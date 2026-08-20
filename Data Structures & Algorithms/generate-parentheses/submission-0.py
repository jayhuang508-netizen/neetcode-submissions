class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        substring = ""
        def dfs(left, right):
            nonlocal substring
            # left is going to decrease
            # right is increasing while left is decrease
            if left == right == n:
                res.append(substring)
                return 
            if left < n:
                substring += "("
                dfs(left+1, right)
                substring = substring[:-1]
            if right < left:
                substring += ")"
                dfs(left, right+1)
                substring = substring[:-1]
                
        dfs(0,0)
        return res
                
            

        