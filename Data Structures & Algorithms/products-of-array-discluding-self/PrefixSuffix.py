#Algorithm
#Let n be the length of the array.
#Create three arrays of size n:
#pref for prefix products
#suff for suffix products
#res for the final result
#Set:
#pref[0] = 1 (nothing to the left of index 0)
#suff[n - 1] = 1 (nothing to the right of last index)
#Build the prefix product array:
#For each i from 1 to n - 1:
#pref[i] = nums[i - 1] × pref[i - 1]
#Build the suffix product array:
#For each i from n - 2 down to 0:
#suff[i] = nums[i + 1] × suff[i + 1]
#Build the result:
#For each index i, compute:
#res[i] = pref[i] × suff[i]
#Return the result array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            pref=nums[0:i]
            suff=nums[(i+1):(len(nums)+1)]

            prodF=1
            for f in pref:
                prodF=f*prodF

            prodL=1
            for l in suff:
                prodL=l*prodL
        
            product=prodF*prodL
            output.append(product)

        return output

#time: O(n)
#space: O(n)
