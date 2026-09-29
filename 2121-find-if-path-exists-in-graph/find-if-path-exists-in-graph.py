class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans = False
        vis = [0]*(n)
        def f(node):
            nonlocal ans
            vis[node] = 1
            if node==destination:
                ans = True
                return ans
            for neigh in adj[node]:
                if vis[neigh]==0:
                    vis[neigh] = 1
                    f(neigh)
        f(source)
        return ans
        

        