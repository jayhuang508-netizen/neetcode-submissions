class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]
        for price in prices:
            profit = max(profit, price-minBuy)
            minBuy = min(price, minBuy)
        return profit