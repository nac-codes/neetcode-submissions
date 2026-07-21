class Solution:
    
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i: int, j: int) -> int:
            queue = [(i,j)]            
            grid[i][j] = 0

            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            
            total_area = 0
            while queue:
                r, c = queue.pop()
                total_area+=1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 0
            
            return total_area

            

        max_area = 0
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 1:
                    max_area = max(dfs(i,j), max_area)

        return max_area

        