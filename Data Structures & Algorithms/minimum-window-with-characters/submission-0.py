#Qn: Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. 
If such a substring does not exist, return an empty string "". You may assume that the correct output is always unique.
#Algorithm
If t is empty, return "".
Build a frequency map countT for characters in t.
Initialize:
window as an empty map for the current window counts.
have = 0 = how many characters currently meet the required count.
need = len(countT) = how many distinct characters we need to match.
res = [-1, -1] and resLen = infinity to store the best window.
Use a right pointer r to expand the window over s:
Add s[r] to window.
If s[r] is in countT and its count in window matches countT, increment have.
When have == need, the window is valid:
Update the best result if the current window is smaller.
Then shrink from the left:
Decrease the count of s[l] in window.
If s[l] is in countT and its count in window falls below countT, decrement have.
Move l right.
After the loop, return the substring defined by res if found; otherwise, return "".


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

#time: O(n+m)
#space: O(m)
