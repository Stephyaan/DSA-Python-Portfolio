#Algorithm
#Create three hash maps of sets:
#rows to track digits in each row
#cols to track digits in each column
#squares to track digits in each 3×3 sub-box, keyed by (r // 3, c // 3)
#Loop through every cell in the board:
#Skip the cell if it contains ".".
#Let val be the digit in the cell.
#If val is already in:
#rows[r] → duplicate in the row
#cols[c] → duplicate in the column
#squares[(r // 3, c // 3)] → duplicate in the 3×3 box
#Then return false.
#Otherwise, add the digit to all three sets:
#rows[r]
#cols[c]
#squares[(r // 3, c // 3)]
#If the whole board is scanned without detecting duplicates, return true.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue          #move to next loop;dont loop here
                if (board[r][c] in rows[r] or   #if alrdy in hash set of rows=duplicate in that row
                    board[r][c] in cols[c] or    #if alrdy in hash set of cols=duplicate in that col
                    board[r][c] in squares[(r // 3,c // 3)]):     #if alrdy in hash set of squares=duplicate in that square
                    return False

                rows[r].add(board[r][c])     #else add to rows hash,to show the no.alrdy in that row
                cols[c].add(board[r][c])     #add to cols hash, shows alrdy in that col
                squares[(r//3,c//3)].add(board[r][c])   #add to sq hash, shows no.alrdy in that square

        return True

#time:O(n^2)
#space:O(n^2)
