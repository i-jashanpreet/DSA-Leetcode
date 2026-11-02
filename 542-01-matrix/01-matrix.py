from collections import deque
class Solution:
    def updateMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        dist = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return dist


