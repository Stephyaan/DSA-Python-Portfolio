#qn: Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
#Algorithm:
#set maximum length of required string,res=0
#loop through each starting index in string as i
    #create a set,CharSet, to add the elements
    #extend the substring, by moving the j forward from i
         #if s[j] already in charSet, break
         #if s[j] not in charSet, add it to charSet
    #update the res to the length of updated charSet
#return res
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range (len(s)):
            charSet=set()
            for j in range(i,len(s)):
                if s[j] in charSet:
                    break
                else:
                    charSet.add(s[j])
            res=max(res,len(charSet))
        return res
    #time O(n*m)
#space O(m)
