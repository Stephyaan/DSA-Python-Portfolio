#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#Algorithm:
#Sort the array to handle duplicates and enable two-pointer logic.
#Loop through the array using index i:
#Let a = nums[i].
#If a > 0, break (all remaining numbers are positive).
#Skip duplicate values for the first number.
#Set two pointers:
#l = i + 1
#r = len(nums) - 1
#While l < r:
#Compute threeSum = a + nums[l] + nums[r].
#If threeSum > 0, move r left.
#If threeSum < 0, move l right.
#If threeSum == 0:
#Add the triplet to the result.
#Move both pointers inward.
#Skip duplicates at the left pointer.
#Return the list of all valid triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()   #2 pointer only if sorted

        for i, a in enumerate(nums):    #a=nums[i]
            if a > 0:     #positive no. then continue
                break

            if i > 0 and a == nums[i - 1]: #check duplicate and avoiding it;continue to next(a=nums[i],
                                             #if a==nums[i-1] in sorted->duplicate)
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
