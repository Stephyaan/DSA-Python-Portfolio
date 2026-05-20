#You are given an array of non-negative integers height which represent an elevation map. 
#Each value height[i] represents the height of a bar, which has a width of 1.
#Return the maximum area of water that can be trapped between the bars.
#Algorithm:
Set two pointers:
l at the start
r at the end
Track leftMax and rightMax as the tallest walls seen.
While l < r:
If leftMax < rightMax:
Move l right.
Update leftMax.
Add leftMax - height[l] to the result.
Else:
Move r left.
Update rightMax.
Add rightMax - height[r] to the result.
Return the total trapped water.


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r=0,len(height)-1
        leftMax=height[l]
        rightMax=height[r]
        result=0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                result+=(leftMax-height[l])

            else:
                r-=1
                rightMax=max(rightMax,height[r])
                result+=(rightMax-height[r])
        return result

#Time O(n)
#space O(1)
