class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0

        def dfs(i: int, j: int):
            if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
                return
            
            if grid[i][j] == "1":
                grid[i][j] = "0"
            else:
                return
            
            dfs(i-1,j) #down
            dfs(i+1,j) #up
            dfs(i,j+1) #right
            dfs(i,j-1) #left
            
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == "0":
                    continue
                
                dfs(i,j)

                total+=1
        
        return total
                
                

                
