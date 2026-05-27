class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newArray=sorted(nums)
        for i in range(len(nums)):
            if newArray[i]==newArray[i+1]:
                return newArray[i]