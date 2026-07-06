'''You are given a signed 32-bit integer x.
Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.
Solve the problem without using integers that are outside the signed 32-bit integer range.'''
'''Algorithm
Save the original value of x in org so we remember its sign.
Convert x to its absolute value.
Convert the number to a string.
Reverse the string.
Convert the reversed string back to an integer res (this automatically removes leading zeros).
If the original number was negative, make res negative.
Check if res fits in the 32-bit signed integer range:
If it does not, return 0.
Otherwise, return the reversed number.'''

class Solution:
    def reverse(self, x: int) -> int:
        org=x
        x=abs(x) #abs to convert to string
        res=int(str(x)[::-1])  #reverses by converting to string
        
        if org<0:  #make neg to pos
            res*=-1
        
        if res < -(1 << 31) or res > (1 << 31) - 1: #not within 32 range
            return 0
        
        return res

#time:O(1)
#space:O(1)