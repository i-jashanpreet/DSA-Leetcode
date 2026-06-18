class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s = []       
        for i in a:            
            while True:                
                if not s:
                    s.append(i)
                    break                
                last = s[-1]               
                if last > 0 and i < 0:                    
                    if abs(last) > abs(i):
                        break
                    elif abs(last) < abs(i):
                        s.pop()
                        continue
                    else:
                        s.pop()
                        break
                else:
                    s.append(i)
                    break
        return s

    
        
        