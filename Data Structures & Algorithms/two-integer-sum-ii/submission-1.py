class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map=defaultdict(int)
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if map[diff]:
                return [map[diff],i+1]
            map[numbers[i]]=i+1
        