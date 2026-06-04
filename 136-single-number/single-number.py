class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        f = {}
        for i in arr:
            f[i]=f.get(i,0)+1
        for j in f:
            if f[j]==1:
                return j