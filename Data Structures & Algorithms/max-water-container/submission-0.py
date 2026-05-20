class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        for l in range(len(heights)):
            for r in range(l+1,len(heights)):
                area=(r-l)*min(heights[l],heights[r])
                result=max(result,area)
        return result