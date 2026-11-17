from functools import lru_cache
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                length = j-i+1
                min_change = float('inf')
                for d in range(1,length):
                    if length%d!=0: continue
                    change = 0
                    for f in range(i,i+d):
                        ns = ''
                        for p in range(f,j+1,d):
                            ns+=s[p]
                        l = 0
                        r = len(ns)-1
                        while l<=r:
                            if ns[l]!=ns[r]:
                                change+=1
                            l+=1
                            r-=1
                    min_change = min(min_change,change)
                cost[i][j] = min_change
        @lru_cache(None)
        def solve(start,k):
            if k==0:
                if start==n:
                    return 0
                return float('inf')
            if start+2*k>n:
                return float('inf')
            mincost = float('inf')
            for end in range(start+1,n):
                mincost = min(mincost,cost[start][end]+solve(end+1,k-1))
            return mincost
        return solve(0,k)
        