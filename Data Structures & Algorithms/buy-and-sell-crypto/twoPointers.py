#Algorithm
Set two pointers:
lBuy = 0 (buy day)
rSell = 1 (sell day)
maxP = 0 to track maximum profit
While rSell is within the array:
If prices[rSell] > prices[lBuy], compute the profit and update maxProfit.
Otherwise, move lBuy to rSell (we found a cheaper buy price).
Move rSell to the next day.
Return maxProfit at the end.

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
#time:O(n)
#space:O(1)
