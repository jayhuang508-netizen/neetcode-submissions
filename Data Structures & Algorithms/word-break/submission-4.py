class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # try to remember the result 
        if len(s)==0:
            return True
        return self.helper(s, wordDict, "", set())
        
        


    def helper(self, s, wordDict, successPart, successSet):
        if len(s)==0:
            return True
        n = len(s)
        # dp = [False for _ in range(n) ]
        res = False
        for i in range(n-1, -1, -1):
            if s[i:] in wordDict:
                if s[i:]+successPart in successSet:
                    # print(s[i:]+successPart, successSet)
                    res = res and True
                else:
                    successSet.add(s[i:]+successPart)
                    res = res or self.helper(s[:i], wordDict, s[i:]+successPart, successSet)
        return res
        