##Algorithm
##Initialize an empty hash set to store seen values.
##Iterate through each number in the array.
##For each number:
##If it is already in the set, return true because a duplicate has been found.
#Otherwise, add it to the set.
#If the loop finishes without finding any duplicates, return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range (len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

#Time complexity: O(n)
#Space complexity: O(n)
