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