class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        arr = []
        for i in range(len(matrix)):
            c = 0
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    c+=1
            arr.append(c)
        return arr

        