class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = {}
        for i in nums:
            f[i]=f.get(i,0)+1
        for j in f:
            if f[j]>len(nums)/2:
                return j
            