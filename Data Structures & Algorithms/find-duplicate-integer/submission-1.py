class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsH={}
        for i in nums:
            if i in numsH:
                return i
            numsH[i]=1
            