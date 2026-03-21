class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        d = 0
        maxi = 0
        for i in s:
            if i=="(":
                d+=1
                stack.append(i)
            elif i==")":
                if stack:
                    d-=1
                    stack.pop()
            maxi = max(maxi,d)
        return maxi
            

        