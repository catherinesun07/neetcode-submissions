class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = -1
        bestBuy = prices[0]

        for sellPrice in prices:
            maxProfit = max(maxProfit, sellPrice - bestBuy)
            bestBuy = min(bestBuy, sellPrice)
        
        return maxProfit

        