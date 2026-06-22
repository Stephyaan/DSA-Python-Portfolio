'''You are given a string digits made up of digits from 2 through 9 inclusive. Each digit (not including 1) is mapped 
to a set of characters as shown below:A digit could represent any one of the characters it maps to.Return all possible letter 
combinations that digits could represent. You may return the answer in any order.'''
'''algorithm:
create array res to store result
create dict digToChar to map digits 2-9 to the respective letters.
define recurring function backtrack(i,currStr):
    if len(currStr) created equals len(dig), ->max len possible for string reached:
        append to the result array, and return to stop further and move to next char of digit
    otherwise, for each char mapped by digit, from digits[i]:
        append char to currStr
        perform recurrence function from next index -> i+1,with each char
if digits not empty, start backtracking from 0 at empty string ->(0,"")
return res
'''
#https://chatgpt.com/s/t_6a395e7bd8988191a055c95a95a20c31
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digToChar = {  #as per qn ; dict is easy to map
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        #eg.:23
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            #map each char for each dig with char of next digit
            for c in digToChar[digits[i]]:
                #0,a ; 0->2
                backtrack(i + 1, currStr + c) #backtrack(1,a) ; 1->3

        if digits:
            backtrack(0, "")

        return res
#time:O(n* 4^n) worst case: 9:"wxyz"->4
#space:O(n * 4^n) worst case output or O(n) extra space

