#You are given an integer array heights where heights[i] represents the height of the i th bar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.
Algorithm
Initialize res = 0 to track the maximum area found.
Use two nested loops:
Outer loop picks the left line i.
Inner loop picks the right line j > i.
For each pair (i, j):
Compute the height as min(heights[i], heights[j]).
Compute the width as j - i.
Update res with the maximum of its current value and the new area.
After checking all pairs, return res.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result=0
        for l in range(len(heights)):
            for r in range(l+1,len(heights)):
                area=(r-l)*min(heights[l],heights[r])
                result=max(result,area)
        return result
