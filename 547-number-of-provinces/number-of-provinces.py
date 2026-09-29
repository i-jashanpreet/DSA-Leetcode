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
        ans = []
        def f(node,comp):
            vis[node]=True
            comp.append(node)
            for neigh in adj[node]:
                if vis[neigh]==False:
                    f(neigh,comp)
        for node in range(n):
            if vis[node]==False:
                comp =[]
                f(node,comp)
                ans.append(comp)
        return len(ans)
