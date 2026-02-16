class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f = {}
        for i in nums1:
            f[i] = f.get(i,0)+1
        res = []
        for j in nums2:
            if j in f and f[j]>0:
                res.append(j)
                f[j]-=1
        return res
         

        