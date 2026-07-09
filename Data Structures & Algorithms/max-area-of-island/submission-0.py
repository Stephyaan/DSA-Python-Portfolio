'''You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.'''
'''Algorithm
Iterate through every cell in the grid.
When a land cell (1) is found:
    Start bfs from that cell.
    Mark it as visited by setting it to 0.
    Initialize area count to 1.
During bfs:
    Pop a cell from the queue.
    Check its 4 neighbors (up, down, left, right).
    If a neighbor is valid land (1), add it to the queue, mark it 0, and increase area.
After bfs completes, update the maximum area.
Continue scanning the grid.
Return the maximum area found.'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        Rows,Cols=len(grid),len(grid[0])
        area=0

        def bfs(r,c):
            q=deque()
            grid[r][c]=0
            q.append((r,c))
            res=1

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+row,dc+col
                    if (nr<0 or nc<0 or 
                       nr>=Rows or nc>=Cols or
                       grid[nr][nc] == 0):
                       continue

                    q.append((nr,nc))
                    grid[nr][nc] = 0
                    res+=1
            return res
            
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c]==1:
                    area=max(area,bfs(r,c))
        return  area

#time O(m*n)
#space:O(m*n)