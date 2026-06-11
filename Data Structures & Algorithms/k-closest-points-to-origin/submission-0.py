class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sorted on basis of x**2+y**2 (neednt use sqrt to sort,as smaller has small sqrt->order wld be same)
        points.sort(key=lambda p:p[0]**2 + p[1]**2)   #p in points->[x,y]
        
        return points[:k]  #k nearest->k smallest dist->first k in sorted list
