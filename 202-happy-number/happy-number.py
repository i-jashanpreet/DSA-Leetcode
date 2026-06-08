class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n!=1:
            if n in visit:
                return False
            visit.add(n)
            s = 0
            for i in str(n):
                s+= int(i)*int(i)
            n = s
        return True
