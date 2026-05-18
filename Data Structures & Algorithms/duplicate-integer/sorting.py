#using sorting : Algorithm
#sort the array in ascending order
#iterate through each element in array starting from index 1.
#compare current element with prev element
#if current and previous elements equals, return true
#else if for lopp ended without finding duplicates, return false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

#time complexity: O(nlogn)
#space complexity: O(n) or O(1)
