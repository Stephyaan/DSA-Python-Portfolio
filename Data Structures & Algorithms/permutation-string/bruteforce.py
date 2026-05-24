#Qn: You are given two strings s1 and s2. Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true. Both strings only contain lowercase letters.
#Algorithm:
#Sort the string 1 so we can compare strings against it.
#loop through each character,i, in string 2
  #from i,move forward through string 2 for ending index j>=i
    #at each j, Extract the substring s2[i : j + 1].
    #check if sorted substring matches the sorted string 1.
    #if then return true.
#if no substring in string 2 when sorted matches the sorted string 1 till end then return false.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)

        for i in range(len(s2)):
            for j in range(i,len(s2)):  #len of smallest substr is 2
                substr=s2[i:j+1]        #j+1 to include i&j(smallest size substr case)
                if sorted(substr)==s1:
                    return True
        return False
        
#time:O(n^3 logn)
#space: O(n)
#not the optimal solution



        
