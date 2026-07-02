class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])

        vis = set()
        dp = {}

        def dfs(i, j, h):

            h -= grid[i][j]

            if h <= 0:
                return False

            if i == m - 1 and j == n - 1:
                return True

            if (i, j, h) in dp:
                return dp[(i, j, h)]

            vis.add((i, j))

            ans = False

            for x, y in [[1,0],[-1,0],[0,1],[0,-1]]:

                ni = i + x
                nj = j + y

                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis:

                    if dfs(ni, nj, h):
                        ans = True
                        break

            vis.remove((i, j))

            dp[(i, j, h)] = ans

            return ans

        return dfs(0, 0, health)

        