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

'''algorithm:
create 2 arrays:
    start->with all start values of intervals sorted
    end->with end values of all intervals sorted
initialize count,res to 0 to maintain the max count of rooms needed
initialize pointers s and e to loop through start and end arrays
loop while value pointed in start<len(intervals):
    if cur start val,s,< the cur end value,e:
        new meeting started before earler ended
        increment s+1, move frwd
        increment count+1
    else if start value,s,reached end value or beyond end value:
        meeting ended
        increment e, move frwd
        decrement count, a room freed, 
update res with max count of rooms, res=max(count,res)
return res for max no.of rooms required
'''