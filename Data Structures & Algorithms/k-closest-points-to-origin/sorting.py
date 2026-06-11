'''You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
Return the k closest points to the origin (0, 0).vThe distance between two points is defined as the 
Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)). You may return the answer in any order.'''
'''Algortihm:
compute dist of points using d = x^2 + y^2
sort the points based on distance in ascending order
return the first k points from sorted list
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sorted on basis of x**2+y**2 (neednt use sqrt to sort,as smaller has small sqrt->order wld be same)
        points.sort(key=lambda p:p[0]**2 + p[1]**2)   #p in points->[x,y]
        
        return points[:k]  #k nearest->k smallest dist->first k in sorted list
#time:O(n log n)
#space:O(n) / O(1) based on sorting
