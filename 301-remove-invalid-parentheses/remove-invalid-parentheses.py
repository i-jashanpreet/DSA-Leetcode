class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []
        left = 0
        right = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        def valid(x):
            bal = 0
            for ch in x:
                if ch == '(':
                    bal += 1
                elif ch == ')':
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        def f(i, curr, removed):
            if i == len(s):
                x = "".join(curr)
                if removed == left + right and valid(x):
                    if x not in ans:
                        ans.append(x)
                return
            curr.append(s[i])
            f(i + 1, curr, removed)
            curr.pop()
            if s[i] == '(' or s[i] == ')':
                f(i + 1, curr, removed + 1)
        f(0, [], 0)
        return ans       