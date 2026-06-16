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
        