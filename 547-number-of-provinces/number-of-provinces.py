class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        ans = 0
        def f(node):
            vis[node] = True
            for neigh in range(n):
                if isConnected[node][neigh] == 1 and vis[neigh] == False:
                    f(neigh)
        for node in range(n):
            if vis[node] == False:
                ans += 1
                f(node)
        return ans
