class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)+1
        while a<=b:
            total = a*a+b*b
            if total==c:
                return True
            elif total>c:
                b-=1
            else:
                a+=1
        return False

     