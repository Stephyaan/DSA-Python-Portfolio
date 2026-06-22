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
        


        