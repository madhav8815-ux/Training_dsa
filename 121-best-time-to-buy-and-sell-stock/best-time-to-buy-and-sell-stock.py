from ast import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
                
            if prices[i] > buyingPrice:
                profit = max(profit, (prices[i] - buyingPrice))
            if buyingPrice > prices[i]:
                buyingPrice = prices[i]
        return profit