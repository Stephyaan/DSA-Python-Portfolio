'''You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. 
For example, the array nums = [1,2,3,4,5,6] might become:[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?'''
'''Algorithm:
loop through each index in list nums
     compare element at each index with target
     if found, return target index
if not found till end of list, return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

#time:O(n)
#space:O(1)
