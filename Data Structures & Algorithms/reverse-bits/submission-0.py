'''Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.'''
'''algorithm:
initialize variable res=0 to store reversed number
for each bit position i from 0-31:
    extract each bit
    shift the position to 31-i
    add to res
after moving till last bit return res
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        #input:bin
        #output:decimal of rev bin
        # & with 1 gives the bin digit there:1&1=1;0&1=0
        res=0
        for i in range(32):
            bit=(n>>i)&1
            res=res|(bit<<(31-i))
        return res

#time:O(1)
#space:O(1)