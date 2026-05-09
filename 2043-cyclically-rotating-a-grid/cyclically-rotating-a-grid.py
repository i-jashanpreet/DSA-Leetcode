class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        layers = min(m, n) // 2
        for layer in range(layers):
            top = left = layer
            bottom = m - layer - 1
            right = n - layer - 1
            pos = []
            for j in range(left, right + 1):
                pos.append((top, j))
            for i in range(top + 1, bottom + 1):
                pos.append((i, right))
            for j in range(right - 1, left - 1, -1):
                pos.append((bottom, j))
            for i in range(bottom - 1, top, -1):
                pos.append((i, left))
            arr = []
            for r, c in pos:
                arr.append(grid[r][c])
            rot = k % len(arr)
            arr = arr[rot:] + arr[:rot]
            for i in range(len(pos)):
                r, c = pos[i]
                grid[r][c] = arr[i]
        return grid
