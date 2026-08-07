class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose the window has the largest gap
        # the number in array has time order
        profit = 0
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1]-prices[0])
        l, r = 0, 1
        n = len(prices)
        while r<n:
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit
        
        