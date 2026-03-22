class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if i==")" and last!="(":
                    return False
                elif i=="]" and last!="[":
                    return False
                elif i=="}" and last!="{":
                    return False
        if len(stack)==0:
            return True
        else:
            return False

    

        

        