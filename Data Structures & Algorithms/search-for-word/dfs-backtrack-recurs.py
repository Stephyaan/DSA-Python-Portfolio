'''Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. 
The same cell may not be used more than once in a word.'''
'''algorithm:
initialise ROWS,COLS=len of rows, len of cols
define recursive function dfs(r,c,i) where i is pos in word we need to match:
    if i at len(word):
        found,return True
    if row,col less than 0 or r,c > ROWS,COLS, or,
    cur pos in board not char in word, or
    position alrdy in path:
        return false
    add (r,c) to path as alrdy visited
    recurse to adjacent 4 neighbours
    unmark (r,c) backtrack
if any start cell answer is true, return true, else false
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #recursive backtracking
        #get len of rows,col
        ROWS,COLS=len(board),len(board[0])
        path=set() #cant revisit->so store visited 

        def dfs(r,c,i):
            #->found
            if i==len(word): #when len of word matches positions covered
                return True
            
            #not found->
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            #char found looking to
            path.add((r,c))  #row,col added to path->found
            res = (dfs(r + 1, c, i + 1) or #look into all adjacent position to see next char from word->return
                dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r,c)) #remove position added to path recent->neednt visit again
            return res

        #for all single start pos run dfs
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

#time:O(n*m*4*n) 4 adjacent pos search required
#space:O(n) len of word
        

