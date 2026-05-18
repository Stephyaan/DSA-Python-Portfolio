## Brute Force: Algorithm
##Iterate through the array with two nested loops using indices i and j to check every pair of different elements.
##If the sum of the pair equals the target, return the indices of the pair.
##If no such pair is found, return an empty array.
##There is guaranteed to be exactly one solution, so we will never return an empty array.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
               ## if (i != j):
                    if (nums[i]+nums[j]==target):
                        return [i,j]

# Time & Space Complexity
#Time complexity: O(n2)
#Space complexity: O(1)

##Hash Map : Algorithm
##Create a hash map to store the value and index of each element in the array.
##Iterate through the array using index i and compute the complement of the current element, which is target - nums[i].
##Check if the complement exists in the hash map.
##If it does, return the indices of the current element and its complement.
##If no such pair is found, return an empty array.

class Solution:
    def twoSum(self, nums:List[int],target:int) -> List[int]:
        prevMap={}   #val:index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i

## The enumerate() function in Python adds a counter to an iterable and returns it as an enumerate object. 
            ## It is the standard way to loop through a list while keeping track of both the index and the value without manually managing a counter variable. 
