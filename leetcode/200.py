class Solution:
    def numIslands(self, grid) -> int:
        answer = 0
        n,m = len(grid),len(grid[0])
        
        def dfs(x,y,n,m,grid):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == "0": return
            grid[x][y] = "0"
            
            dfs(x,y+1,n,m,grid)
            dfs(x,y-1,n,m,grid)
            dfs(x+1,y,n,m,grid)
            dfs(x-1,y,n,m,grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i,j,n,m,grid)
                    answer += 1
                
        
        return answer

