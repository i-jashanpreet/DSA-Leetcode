class Solution:
    def assignEdgeWeights(self, edges, queries):
        from collections import defaultdict
        import math
        n = len(edges) + 1
        mod = 10**9 + 7
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        LOG = math.ceil(math.log2(n)) + 1
        up = [[0] * LOG for _ in range(n + 1)]
        dep = [0] * (n + 1)
        def dfs(u, p):
            up[u][0] = p
            for i in range(1, LOG):
                up[u][i] = up[up[u][i - 1]][i - 1]
            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)
        dfs(1, 0)
        def lca(a, b):
            if dep[a] < dep[b]:
                a, b = b, a
            d = dep[a] - dep[b]
            for i in range(LOG):
                if d & (1 << i):
                    a = up[a][i]
            if a == b:
                return a
            for i in range(LOG - 1, -1, -1):
                if up[a][i] != up[b][i]:
                    a = up[a][i]
                    b = up[b][i]
            return up[a][0]
        ans = []
        for u, v in queries:
            x = lca(u, v)
            d = dep[u] + dep[v] - 2 * dep[x]
            if d == 0:
                ans.append(0)
            else:
                ans.append(pow(2, d - 1, mod))
        return ans
        