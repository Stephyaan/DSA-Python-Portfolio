"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])

        res,count=0,0  #keep count of rooms and store max rooms in res

        s,e=0,0 #to keep track along each start&end list

        while s<len(intervals): #s adds first;so if it didnt reached end
            if start[s]<end[e]:
                s+=1
                count+=1

            else:
                e+=1
                count-=1
            
            res=max(res,count)

        return res