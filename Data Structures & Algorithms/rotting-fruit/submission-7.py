class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: #fresh
                    fresh += 1
                if grid[r][c] == 2: #rot
                    q.append((r, c)) #rot so add to queue

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]#adj pos
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft() #take latest rot to look its neighbours

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2 #make neighbours rot
                        q.append((row, col)) #rot added to q
                        fresh -= 1 #update fresh count
            time += 1 #time count plus
        return time if fresh == 0 else -1
    
