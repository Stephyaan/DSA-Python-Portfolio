'''Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
Return an array output where output[i] is the number of 1's in the binary representation of i.'''
'''algorithm:
create the empty array for output
for the each integer i in the range [0,n]:
    convert i to binary representation
    take count of 1s in binary form
    append the count to res array
return res array after every integer in range [0,n]
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            output.append(bin(i).count('1'))

        return output
    #time:O(nlogn)
    #space:O(n)
        