'''You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.Open brackets are closed in the correct order.
 Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.'''
''' Algorithm:
While the string still contains "()", "{}", or "[]":
Remove all occurrences of those pairs.
After no more pairs can be removed:
If the string is empty, return true.
Otherwise, return false.
'''
Sol:
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s: #loop through characters in s to check if has '()' or '[]' or '{}' :
            s=s.replace('()','')         #remove/replace with empty string ''
            s=s.replace('{}','')
            s=s.replace('[]','')
        return s==''            #lastly if no more paired brackets,s is empty=return true;else s has unpaired brackets left, s not empty=return false, 
#time:O(n^2)
#Space:O(n)

        
