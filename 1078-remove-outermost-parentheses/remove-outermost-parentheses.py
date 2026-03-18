class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        stack=[]
        for i in s:
            if i=="(":
                if stack:
                    res+=i
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res+=i
        return res



        