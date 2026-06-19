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
        

