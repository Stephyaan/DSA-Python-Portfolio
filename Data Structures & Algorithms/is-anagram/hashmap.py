#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#algorithm:
#if 2 strings have different length, return False immediately
#create 2 hashsets for both strings
#iterate through both strings at same time
#increment count of s[i]
# increase the count of t[i]
#compare the both maps,
#if equal, return True
#else return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
#T(n)=O(n+m)
#Space O(1)
