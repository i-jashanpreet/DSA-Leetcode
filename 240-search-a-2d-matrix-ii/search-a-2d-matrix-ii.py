class Solution:
    def searchMatrix(self, mat: List[List[int]], t: int) -> bool:
        m=len(mat[0])
        n=len(mat)
        row=0
        col=m-1
        while row<n and col>=0:
            if mat[row][col]==t:
                return True
            elif mat[row][col]<t:
                row+=1
            else:
                col-=1
        return False
        

        