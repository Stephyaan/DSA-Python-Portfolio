#qn: You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
#The lowest price so far → this is the best day to buy.
The best profit so far → selling today minus the lowest buy price seen earlier.
#Algorithm
#Initialize:
#minBuy as the first price
#maxP = 0 for the best profit
#Loop through each price sell:
#Update maxP with sell - minBuy.
#Update minBuy if we find a smaller price.
#Return maxP after scanning all days.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyMin=prices[0]
        sellMax=0
        for p in prices:
            sellMax=max(sellMax,(p-buyMin))
            buyMin=min(buyMin,p)
        return sellMax

#time: O(n)
#space:O(1)
