class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0]*n
        for i in range(n):
            if i == 0:
                array[i] = 1
            elif i == 1:
                array[i] = 2
            else:
                array[i] = array[i-1] + array[i-2]
            
        return array[n-1]
            
        