class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if stack:
                    x=stack.pop()
                    if i==")" and x!="(" or i=="}" and x!="{" or i=="]" and x!="[":
                        return False
                else:
                    return False
        if len(stack)!=0:
            return False
        return True

        

        