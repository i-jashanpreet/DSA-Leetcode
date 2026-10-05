# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         vis = [False] * n
#         ans = 0
#         def f(node):
#             vis[node] = True
#             for neigh in range(n):
#                 if isConnected[node][neigh] == 1 and vis[neigh] == False:
#                     f(neigh)
#         for node in range(n):
#             if vis[node] == False:
#                 ans += 1
#                 f(node)
#         return ans


from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        ans = 0
        def bfs(node):
            queue = deque()
            queue.append(node)
            vis[node] = True
            while queue:
                e = queue.popleft()
                for neigh in range(n):
                    if isConnected[e][neigh] == 1 and vis[neigh] == False:
                        vis[neigh] = True
                        queue.append(neigh)
        for node in range(n):
            if vis[node] == False:
                ans += 1
                bfs(node)
        return ans