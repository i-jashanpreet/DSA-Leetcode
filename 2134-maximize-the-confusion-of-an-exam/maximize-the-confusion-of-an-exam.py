class Solution:
    def maxConsecutiveAnswers(self, ak: str, k: int) -> int:
        i = 0
        t = 0
        f = 0
        ans= 0
        for j in range(len(ak)):
            if ak[j]=="T":
                t+=1
            else:
                f+=1
            while min(t,f)>k:
                if ak[i]=="T":
                    t-=1
                else:
                    f-=1
                i+=1
            ans = max(ans, j - i + 1)
        return ans


