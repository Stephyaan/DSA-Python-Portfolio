#Algorithm
#Create an empty string newStr.
#Loop through each character c in the input string:
#If c is alphanumeric, convert it to lowercase and add it to newStr.
#Compare newStr with its reverse (newStr[::-1]):
#If they are equal, return true.
#Otherwise, return false.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS=""
        revS=""
        for c in s:
            if c.isalnum():
                newS+=c.lower()
        revS=newS[::-1]

        return newS==revS    

#time:O(n)
#space:O(n)
