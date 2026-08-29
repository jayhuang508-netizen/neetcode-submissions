class Solution:
    def countSubstrings(self, s: str) -> int:
        # check how many True in the dp matrix
        # or directly count how many palindromic encounters
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0
        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1] == True):
                    count += 1 
                    dp[i][j] = True
        return count
        