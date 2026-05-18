#For example

#All numbers that appear 1 time go into group freq[1].
#All numbers that appear 2 times go into group freq[2].
#And so on.

#Algorithm
#Build a frequency map that counts how many times each number appears.
#Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
#For each number and its frequency in the map, add the number to freq[frequency].
#Initialize an empty result list.
#Loop from the largest possible frequency down to 1:
#For each number in freq[i], add it to the result list.
#Once the result contains k numbers, return it.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)

        freq=[[] for i in range (len(nums)+1)]    #bucket list with counts to indicate with num
        for num,count in count.items():
            freq[count].append(num)

        result=[]
        for i in range((len(freq)-1),0,-1):
            for num in freq[i]:
                result.append(num)
                if len(result)==k:
                    return result
