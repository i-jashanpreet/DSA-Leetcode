class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                if stack:
                    stack.pop()
            elif i == "#":
                stack.extend(stack)
            elif i == "%":
                stack.reverse()
            else:
                stack.append(i)
        return ''.join(stack)


        