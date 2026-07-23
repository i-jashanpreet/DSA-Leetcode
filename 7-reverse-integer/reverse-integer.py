class Solution(object):
    def reverse(self, x):
        # INT_MAX = 2**31 - 1
        # INT_MIN = -2**31
        # rev = 0
        # sign = 1
        # if x < 0:
        #     sign = -1
        #     x = -x
        # while x != 0:
        #     digit = x % 10
        #     x = x // 10
        #     if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
        #         return 0
        #     rev = rev * 10 + digit
        # return sign * rev

        maxi = 2**31-1
        ans = 0
        if x<0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        while x:
            ld = x%10
            x = x//10
            if ans>maxi//10 or (ans==maxi and ld>7):
                return 0
            ans = ans*10+ld
        return ans*sign




        
        