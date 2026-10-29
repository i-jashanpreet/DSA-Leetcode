
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 0
                    area = 0
                    while stack:
                        x, y = stack.pop()
                        area += 1
                        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < m and 0 <= ny < n
                                    and grid[nx][ny] == 1):
                                grid[nx][ny] = 0
                                stack.append((nx, ny))
                    maxi = max(maxi, area)
        return maxi

