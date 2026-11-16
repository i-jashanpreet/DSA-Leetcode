class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        while n > k:
            new = ""
            j = 0
            while j < n:
                sumi = 0
                for i in range(j, min(j + k, n)):
                    sumi += int(s[i])
                new += str(sumi)
                j += k
            s = new
            n = len(s)
        return s






        