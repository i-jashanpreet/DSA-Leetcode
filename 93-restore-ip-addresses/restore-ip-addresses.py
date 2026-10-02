class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans =[]
        curr = []
        def f(i):
            if len(curr)==4 and i==len(s):
                ans.append(".".join(curr))
                return
            for j in range(i,min(i+3,len(s))):
                x = s[i:j+1]
                if len(x)>1 and x[0]=="0":
                    continue
                if int(x)>255:
                    continue
                curr.append(x)
                f(j+1)
                curr.pop()
        f(0)
        return ans        