'''You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, 
which represents the number of hours you have to eat all the bananas.You may decide your bananas-per-hour eating rate of k. 
Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
you may finish eating the pile but you can not eat from another pile in the same hour.Return the minimum integer k such that you can 
eat all the bananas within h hours.Example 1:Input: piles = [1,4,3,2], h = 9 ; Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, 
you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
Example 2:Input: piles = [25,10,23,4], h = 4; Output: 25'''
'''Algotithm:
Set the search range:
left = 1 (minimum possible speed)
right = max(piles) (maximum needed speed)
While left <= right:
Let mid be the current speed to test.
Compute the total hours needed using this speed.
If the total hours is within the allowed time h:
This speed works, so record it.
Try to find a smaller working speed by searching the left half.
Otherwise:
Speed is too slow, so search in the right half.
After the search ends, return the smallest valid speed found.
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours<=h:
                res=min(res,k)
                r=k-1    
            else:
                l=k+1    

        return res

#time:O(n*log m)
#space:O(1)
