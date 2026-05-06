class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        rotated = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]
        for j in range(m):
            empty = n - 1
            for i in range(n - 1, -1, -1):
                if rotated[i][j] == '*':
                    empty = i - 1
                elif rotated[i][j] == '#':
                    rotated[i][j] = '.'
                    rotated[empty][j] = '#'
                    empty -= 1
        return rotated
        