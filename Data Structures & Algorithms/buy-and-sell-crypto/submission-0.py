class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyMin=prices[0]
        sellMax=0
        for p in prices:
            sellMax=max(sellMax,(p-buyMin))
            buyMin=min(buyMin,p)
        return sellMax