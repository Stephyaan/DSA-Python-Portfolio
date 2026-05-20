#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#Algorithm:
Algorithm
Sort the array to make handling duplicates easier.
Create an empty set res to store unique triplets.
Use three nested loops:
For each i,
For each j > i,
For each k > j,
Check if nums[i] + nums[j] + nums[k] == 0.
If true, add the sorted triplet to the set.
Convert the set of tuples back into a list of lists.
Return the result.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                for k in range(j+1, len(nums)):

                    if (nums[i] + nums[j] + nums[k]) == 0:

                        temp = sorted([nums[i], nums[j], nums[k]])

                        if temp not in output:
                            output.append(temp)

        return output
