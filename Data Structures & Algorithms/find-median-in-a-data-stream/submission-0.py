'''The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value,
so the median is the mean of the two middle values.Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.'''
'''algorithm:
initialize:
    create an empty list nums
add element num:
    appen element stored in num to list nums
find median:
    check if length odd or even.
    if even: then set median as self.nums[(len(self.nums)//2)]+self.nums[(len(self.nums)//2)-1]) / 2
    else odd: median is self.nums[(len(self.nums)//2)]
return computed median
'''
class MedianFinder:

    def __init__(self):
        self.nums=[]
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums) % 2 == 0:
            m= float((self.nums[(len(self.nums)//2)]+self.nums[(len(self.nums)//2)-1]) / 2)
        else:
            m=self.nums[(len(self.nums)//2)]
       
        #or
        #n=len(self.nums)
        #return (self.data[n // 2] if (n & 1) else
        #       (self.data[n // 2] + self.data[n // 2 - 1]) / 2)

        return float(m)
#time:O(m) for add() and O() formedian O(m*logn)
#space:O(n)
        
