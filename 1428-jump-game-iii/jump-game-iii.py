class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)       
        v = set()       
        def f(i):
            if i < 0 or i >= n:
                return False
            if i in v:
                return False
            if arr[i] == 0:
                return True            
            v.add(i)
            left = f(i - arr[i])
            right = f(i + arr[i])            
            return left or right        
        return f(start)
        