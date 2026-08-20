class Solution:
    def palindrome(self, s):
        if len(s) == 1:
            return True
        i, j = 0, len(s)-1
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def partitionCheck(substring):
            if len(substring) == 0:
                    res.append(subset.copy())
                    return
            for i in range(1, len(substring)+1):
                if self.palindrome(substring[:i]):
                    subset.append(substring[:i])
                    partitionCheck(substring[i:])
                    subset.pop()
                

                
        partitionCheck(s)
        return  res

            

        