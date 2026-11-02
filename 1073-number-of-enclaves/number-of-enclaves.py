class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def f(r,c):
            if r<0 or c<0 or r>=n or c>=m:
                return 
            if grid[r][c]==0:
                return 
            grid[r][c] = 0
            f(r-1,c)
            f(r+1,c)
            f(r,c-1)
            f(r,c+1)
        for j in range(m):
            if grid[0][j]==1:
                f(0,j)
            if grid[n-1][j]==1:
                f(n-1,j)
        for i in range(n):
            if grid[i][0]==1:
                f(i,0)
            if grid[i][m-1]==1:
                f(i,m-1)
        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    c+=1
        return c


