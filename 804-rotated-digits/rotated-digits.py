class Solution:
    def rotatedDigits(self, n: int) -> int:
        c = 0
        for i in range(1,n+1):
            s = str(i)
            valid = True
            diff = False
            for ch in s:
                if ch in "347":
                    valid = False
                    break
                if ch in "2569":
                    diff = True
            if valid and diff:
                c+=1
        return c
        