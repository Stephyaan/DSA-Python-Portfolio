'''You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
You may assume n is a non-negative integer which fits within 32-bits.'''
'''algorithm:
create res=0 to store cnt
for each bit position i in range 32:
    create mask with only ith bit set:
    mask=1<<i
if bit set in mask,(mask & n) != 0 then increment res
after checking all 32 bits,return res
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        for i in range(32):
            if (1<<i) & n: #mask=(1<<i)
                res+=1
        return res

    #time:O(1)
    #space:O(1)