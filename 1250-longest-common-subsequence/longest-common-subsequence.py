class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = [[-1]*m for _ in range(n)]
        def f(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if text1[i]==text2[j]:
                memo[i][j] =  1 + f(i+1,j+1)
            else:
                memo[i][j] =  max(f(i+1,j),f(i,j+1))
            return memo[i][j]
        return f(0,0)
