class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = set()
        def dfs(u, d):
            vis.add(u)
            mx = d
            for v in g[u]:
                if v not in vis:
                    mx = max(mx, dfs(v, d + 1))
            return mx
        d = dfs(1, 0)
        return pow(2, d - 1, 10**9 + 7)
        