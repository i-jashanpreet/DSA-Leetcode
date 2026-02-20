class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        p = 1
        s = 0
        for i in n:
            p = p*int(i)
            s = s+int(i)
        return p-s

        