'''Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).'''
'''algorithm:
set rows=len(grid) and cols=len(grid[0])
initilaize set,visit to store visited elements, and islands=0, the count of island groups
if grid=0,return 0 stop
define iterative function bfs(r,c):
    create queue to store the visited positions
    add each (r,c) to visited and append to queue

    while q not empty:
        pop from left end of q the last element entered as cur row an cur col
        take directions 

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:  #if no grid;nothing to do
            return 0
        
        rows,cols=len(grid),len(grid[0])
        visit=set() #store visited
        islands=0 #count
        
        def bfs(r,c): #iterative
            q=collections.deque() #queue for bfs to store
            visit.add((r,c))  #append to visit each (r,c) once visited
            q.append((r,c)) #once viisted, append to queue
            
            while q: #q not empty
                row,col=q.popleft()  #to change to dfs->change popleft() to pop()
                directions=[[1,0],[-1,0],[0,1],[0,-1]] #move to any of adjacent direction

                for dr,dc in directions: #go through each of 4 dir
                    r,c=row+dr,col+dc #take rows&cols of each direction adj element
                    if ((r) in range(rows) and
                        (c) in range(cols) and 
                        grid[r][c] =="1" and
                        (r,c) not in visit):
                        q.append((r,c))   #as each of 4 adj visited, add to queue
                        visit.add((r,c)) #append (r,c) to set as visited
        
        #start from row=0 and col=0
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands