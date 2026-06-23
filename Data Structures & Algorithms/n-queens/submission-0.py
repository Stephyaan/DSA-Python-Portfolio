class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #1st try each pos in 1st row
        #then move to next rows and check
        
        col=set() #col set to maintain cols filled
        posDiag=set() #pos diagnols=r+c
        negDiag=set()  #neg diagnol=r-c

        res=[]
        board=[['.']*n for i in range(n)] #board col with no Q-> "."

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                #cant place in same col set or neg/pos diagnol set->skip
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                #safe; add col,diagnols to resp set to not use again
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c]="Q"

                backtrack(r+1) #recurse to next row

                #remove all col,diagnol elements->backtracking
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."
        
        backtrack(0)

        return res

    
    

