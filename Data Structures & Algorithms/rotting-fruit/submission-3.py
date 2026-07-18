from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:                           
        queue = deque()        
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        turn_count = 0
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 2:
                    queue.append((i,j,0))
        
        while queue:
            r, c, turns = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if 0<=nr<len(grid) and 0<=nc<len(grid[nr]):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc,turns+1))
            
            turn_count=turns
        

        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 1:
                    return -1
        
        return turn_count
                    
        

