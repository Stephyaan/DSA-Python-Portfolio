'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.
A queen in a chessboard can attack horizontally, vertically, and diagonally.Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.
You may return the answer in any order.'''
'''Algorithm
Use three hash sets:
col → tracks used c (columns)
posDiag → tracks (row + col)
negDiag → tracks (row - col)
Initialize an empty n x n board with ".".
Start backtracking from row 0.
For the current r (row):
Try every c (column)
If c, (r + c), or (r - c) is already in the sets → skip
If safe:
Add c, (r + c), (r - c) to the sets
Place "Q" on the board
Recurse to the next row
If all rows are filled:
Convert the board into a list of strings and save it
Backtrack:
Remove the queen from the board
Remove entries from all sets
Continue until all valid configurations are found.
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #1st try each pos in 1st row
        #then move to next rows and check
        
        col=set() #col set to maintain cols filled
        posDiag=set() #pos diagnols=r+c
        negDiag=set()  #neg diagnol=r-c

        res=[]
        board=[['.']*n for i in range(n)] #board col with no Q-> "." , Creates an empty chessboard.

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
#time : O(n!)
#space: O(n^2)

        return res

    
    

