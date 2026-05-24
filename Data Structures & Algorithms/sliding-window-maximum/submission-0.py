class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxL=[]
        for i in range(len(nums)):
            if len(nums[i:(i+k)]) < k:
                break
            maxL.append(max(nums[i:(i+k)]))
        return maxL
