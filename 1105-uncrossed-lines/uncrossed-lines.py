class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m =len(nums2)
        memo = [[-1]*m for _ in range(n)]
        def f(i,j):
            if i==n or j==m:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if nums1[i]==nums2[j]:
                memo[i][j]= 1 + f(i+1,j+1)
            else:
                memo[i][j] =  max(f(i+1,j),f(i,j+1))
            return memo[i][j]
        return f(0,0)
        