'''You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.Note: This chart is known as a histogram.
Example 1: Input: heights = [7,1,7,2,2,4] ; Output: 8
Example 2: Input: heights = [1,3,7] ; Output: 7 '''
'''Algorithm:
For every starting position:
Set minimum height to the current bar.
Extend the rectangle to the right.
Update the minimum height seen so far.
Area = minimum height × width.
Keep track of the maximum area.
'''
sol:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        for l in range(len(heights)):
            minHeight=heights[l]

            for r in range(l,len(heights)):
                minHeight=min(minHeight,heights[r])
                area=(minHeight*(r-l+1))
                maxArea=max(maxArea,area)

        return maxArea

#time:O(n^2)
#space:O(1)
