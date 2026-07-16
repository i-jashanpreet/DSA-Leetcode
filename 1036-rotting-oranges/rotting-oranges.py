class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_orange = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh_orange+=1
        
        min = 0
        while len(q)!=0 and fresh_orange>0:
            min+=1
            total_rotten = len(q)
            for _ in range(total_rotten):
                i,j = q.popleft()
                for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    new_i,new_j = i+dx,j+dy
                    if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                        continue
                    if grid[new_i][new_j]==2 or grid[new_i][new_j]==0:
                        continue
                    fresh_orange-=1
                    grid[new_i][new_j]=2
                    q.append((new_i,new_j))
        if fresh_orange>0:
            return -1
        return min           
        