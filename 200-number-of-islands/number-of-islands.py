class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        def f(i,j):
            if i>=m or i<0 or j>=n or j<0:
                return 
            if grid[i][j]=="0":
                return
            if grid[i][j]=="1":
                grid[i][j]="0"
            f(i-1,j)
            f(i+1,j)
            f(i,j-1)
            f(i,j+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    c+=1
                    f(i,j)
        return c

        


        