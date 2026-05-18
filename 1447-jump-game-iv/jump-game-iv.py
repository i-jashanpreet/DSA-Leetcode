class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)        
        if n == 1:
            return 0
        mp = {}       
        for i in range(n):           
            if arr[i] not in mp:
                mp[arr[i]] = []            
            mp[arr[i]].append(i)        
        q = [0]        
        visited = set()
        visited.add(0)        
        steps = 0       
        while q:            
            size = len(q)           
            for _ in range(size):                
                i = q.pop(0)
                if i == n - 1:
                    return steps               
                neighbors = []
                if arr[i] in mp:
                    neighbors += mp[arr[i]]
                neighbors.append(i - 1)
                neighbors.append(i + 1)                
                for nxt in neighbors:                    
                    if 0 <= nxt < n and nxt not in visited:                        
                        visited.add(nxt)
                        q.append(nxt)
                mp[arr[i]] = []            
            steps += 1