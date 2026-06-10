'''algorithm:
initialization():
store nums to arr
store k t

add(val):
append val to arr
sort arr
return the kth largest value, at len(self.arr)-self.k position in arr
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.arr=nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return (self.arr[len(self.arr)-self.k])

#time:O(m*n logn)   m=no.of calls made to add()
#space:O(n)/O(1) depends on sorting
      #or O(m)

