'''Algorithm:
convert integer to binary form
take count the of 1s in intger
return the count of 1s
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
            