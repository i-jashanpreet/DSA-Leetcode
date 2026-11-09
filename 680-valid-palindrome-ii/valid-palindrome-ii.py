class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispali(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return ispali(i,j-1) or ispali(i+1,j)
        return True
        