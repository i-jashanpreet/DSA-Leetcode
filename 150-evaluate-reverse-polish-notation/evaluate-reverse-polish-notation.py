class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+*-/":
                b = int(stack.pop())
                a = int(stack.pop())
                if i=="+":
                    res = a+b
                    stack.append(res)
                if i=="-":
                    res = a-b
                    stack.append(res)
                if i=="*":
                    res = a*b
                    stack.append(res)
                if i=="/":
                    res = a/b
                    stack.append(res) 
            else:
                stack.append(i)
        return int(stack[-1])                  

        