'''Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
You may return the solution in any order. Example 1:
Input: s = "aab" ; Output: [["a","a","b"],["aa","b"]] '''
'''algorithm:
initialise result array res
initilise pallindrome partition array part
define recursive function dfs(i):
    if i points out of bound len(s):
        append the copy of part to the res and return
    check if pallindrome for from i..j(s[i..j]):
        if then add s[i:j+1] to part
        continue recursion dfs from next j+1
        backtracking: remove the last substring
define function isPallin(s,l,r):
    while l<r, check if s[l:r] pallindrome->return true, else false
    move left and right pointerss
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[] #store all lists of pallin set

        part=[] #store each pallin combination

        def dfs(i): #pointer
            if i>=len(s): #completed all elements
                res.append(part.copy()) #append rem part to result
                return
            
            for j in range(i,len(s)):
                if self.isPallin(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def isPallin(self,s,l,r):
        while l<r:
            if s[l] != s[r]:
                return False
            l,r=l+1,r-1
        return True
#time:O(n*2^n)
#space:O(n) if extra space or O(n*2^n) for output list


        
