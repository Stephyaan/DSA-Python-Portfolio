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
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3,c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True

#time:O(n^2)
#space:O(n^2)
