'''You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.Your solution must run in O(logn) time. '''
'''Algorithm:
loop through each integer element in list nums by its index
   compare the element at each index with target integer
   if found, return index
if not found till final index, return -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

#time:O(n) ; checks every element
#space :O(1)
