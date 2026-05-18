class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash={}
        for num in nums:
            countHash[num]=1+countHash.get(num,0)

        array=[]
        for num,count in countHash.items():
            array.append([count,num])
        array.sort()

        result=[]
        while len(result)<k:
            result.append(array.pop()[1])
        return result
