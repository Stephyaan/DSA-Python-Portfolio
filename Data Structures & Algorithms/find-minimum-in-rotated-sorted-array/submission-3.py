class Solution:
    def findMin(self, nums: List[int]) -> int:
        minm=nums[0]
        for num in nums:
            if num<minm:
                minm=num
        return minm