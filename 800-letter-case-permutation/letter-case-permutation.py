class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        curr = []
        ans = []
        def f(i):
            if i==len(s):
                ans.append("".join(curr))
                return 
            ch = s[i]
            if ch.isalpha():
                curr.append(ch.lower())
                f(i+1)
                curr.pop()
                curr.append(ch.upper())
                f(i+1)
                curr.pop()
            else:
                curr.append(ch)
                f(i+1)
                curr.pop()   
        f(0)
        return ans             