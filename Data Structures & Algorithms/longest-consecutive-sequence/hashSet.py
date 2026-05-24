#qn: Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
#Algorithm
#Convert the list into a set numSet for O(1) lookups.
#Initialize longest to track the length of the longest consecutive sequence.
#For each number num in numSet:
#Check if num - 1 is not in the set:
#If true, num is the start of a sequence.
#Initialize length = 1.
#While num + length exists in the set, increase length.
#Update longest with the maximum length found.
#Return longest after scanning all numbers.
#Longest Consecutive Sequence - HashSet

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)       #Hash Set
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1    #1 start element found (with no preceding no.)
                while (num + length) in numSet:  #check if next consecutive no. in numSet
                    length += 1                  #then increase length of consecutive sequence
                longest = max(length, longest)
        return longest

#Time: O(n)
#Space: O(n)
