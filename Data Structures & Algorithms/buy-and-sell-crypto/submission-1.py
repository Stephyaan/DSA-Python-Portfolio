class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        lBuy,rSell=0,1
        while(rSell<(len(prices))):
            if (prices[lBuy]<prices[rSell]):
                maxProfit=max(maxProfit,(prices[rSell]-prices[lBuy]))
            else:
                lBuy=rSell
            rSell+=1
        return maxProfit
