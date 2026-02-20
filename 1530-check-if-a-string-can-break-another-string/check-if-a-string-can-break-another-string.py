class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        flag = False
        c1 = 0
        for i in range(n):
            if s1[i]>=s2[i]:
                c1 +=1
        if c1==n:
            flag = True
        c2 = 0
        for i in range(n):
            if s2[i]>=s1[i]:
                c2 +=1
        if c2==n:
            flag = True
        return flag
        
