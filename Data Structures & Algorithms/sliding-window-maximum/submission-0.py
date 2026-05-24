#Qn: You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. 
The window slides one position to the right until it reaches the right edge of the array.Return a list that contains the maximum element in the window at each step.
#Algorithm:
#Create an empty list, maxL, output to store the maximum of each window.
#For each starting index i from 0 to len(nums):
#check if length of substring between i and i+k < k
    #if yes,break
    #else, append to maxL the maximum in the substring 
#Return output list maxL after checking all windows.
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxL=[]
        for i in range(len(nums)):
            if len(nums[i:(i+k)]) < k:
                break
            maxL.append(max(nums[i:(i+k)]))
        return maxL
#timeO(n*k)
#space O(n)
