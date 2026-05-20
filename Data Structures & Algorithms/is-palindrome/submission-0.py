class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS=""
        revS=""
        for c in s:
            if c.isalnum():
                newS+=c.lower()
        revS=newS[::-1]

        return newS==revS    
        