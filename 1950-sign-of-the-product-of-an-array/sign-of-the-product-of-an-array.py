class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for i in nums:
            p*=i
        def signFunc(x):
            if x>0:
                return 1
            elif x==0:
                return 0
            else:
                return -1
        return signFunc(p)

        