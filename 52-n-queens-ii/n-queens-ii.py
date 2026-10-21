class Solution:
    def totalNQueens(self, n: int) -> int:
        ans= []
        bord = [["."]*n for _ in range(n)]
        def safe(row,col):
            i,j = row,col
            #up direction
            while i>=0:
                if bord[i][j]=="Q":
                    return False
                i-=1
            #left dig
            i,j = row,col
            while i>=0 and j>=0:
                if bord[i][j]=="Q":
                    return False
                i-=1
                j-=1
            #right dag
            i,j = row,col
            while i>=0 and j<n:
                if bord[i][j]=="Q":
                    return False
                i-=1
                j+=1
            return True
        c = 0
        def f(row):
            nonlocal c
            if row==n:
                c+=1
                return
            for col in range(n):
                if safe(row,col):
                    bord[row][col] = "Q"
                    f(row+1)
                    bord[row][col] = "."
        f(0)
        return c        