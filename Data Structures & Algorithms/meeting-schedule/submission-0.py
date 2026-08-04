"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #compare each one with left from start
        for i in range(len(intervals)):
            a=intervals[i]
            for j in range(i+1,len(intervals)):
                b=intervals[j]
                if min(b.end,a.end)>max(a.start,b.start):
                    return False

        return True
