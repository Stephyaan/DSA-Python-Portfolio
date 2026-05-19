class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            partF=nums[0:i]
            partL=nums[(i+1):(len(nums)+1)]

            prodF=1
            for f in partF:
                prodF=f*prodF

            prodL=1
            for l in partL:
                prodL=l*prodL
        
            product=prodF*prodL
            output.append(product)

        return output
        