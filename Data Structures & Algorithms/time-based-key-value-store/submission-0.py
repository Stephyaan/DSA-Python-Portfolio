'''Design a time-based key-value data structure that can store multiple values for the same key at different time stamps 
and retrieve the key's value at a certain timestamp.Implement the TimeMap class: () Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".'''
'''Algorithm
Use a dictionary:
key → list of [value, timestamp]
Timestamps for each key are stored in sorted order (because they arrive in increasing order).
set(key, value, timestamp):
Append [value, timestamp] to the key’s list.
get(key, timestamp):
If the key does not exist, return "".
Let arr be the list of [value, timestamp] pairs.
Perform binary search on timestamps to find the rightmost timestamp t ≤ timestamp.
If found, return the corresponding value.
If not found, return "".
'''
class TimeMap:

    def __init__(self):
        self.timeMap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key]=[]
        self.timeMap[key].append([value,timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.timeMap.get(key,[])
        l,r=0,len(values)-1
        while l<=r:
            m=(l+r)//2
            if (values[m][1]<=timestamp):
                res=values[m][0]
                l=m+1
            else:
                r=m-1
        return res

#time:O(1) for set() and O(logn) for get()
#space:O(m*n)
