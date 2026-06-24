class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp=[] #insert all non zero from nums in order
        for num in nums:
            if num!=0:
                tmp.append(num)

        for i in range(len(nums)):
            if i<len(tmp):
                nums[i]=tmp[i]

            else:
                nums[i]=0

        