'''You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. 
Return the median value among all elements of the two arrays.Your solution must run in O(log(m+n)) time.'''
'''Algorithm:
merge both lists of integers to single list, nums
sort the merged list, nums
compute if no.of elements is odd / even
if odd, compute  and return median by  ( (nums[(len(nums) //2) -1] + nums[len(nums) //2 ] ) / 2.0 )
if even, return median= nums[len(nums) // 2]
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums=sorted(nums)
        if (len(nums) % 2) == 0: #[1, 2, 3, 4];median = (2 + 3) / 2 = 2.5.
            r= ( (nums[(len(nums) // 2) -1] + nums[len(nums) // 2 ]) / 2.0 )
            return float(r)
        else:                 #[1, 2, 3]; median = 2.
            r= nums[len(nums)//2.0] 
            
            return float(r)

#time:O((m+n) log (m+n) )
#space:O(n+m)
