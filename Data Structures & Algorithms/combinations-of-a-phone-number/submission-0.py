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