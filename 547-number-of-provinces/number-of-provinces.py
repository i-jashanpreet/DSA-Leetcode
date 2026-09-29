class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    adj[j].append(i)
        vis = [False]*n
        ans = 0
        def f(node):
            vis[node]=True
            for neigh in adj[node]:
                if vis[neigh]==False:
                    f(neigh)
        for node in range(n):
            if vis[node]==False:
                ans+=1
                f(node)
        return ans
