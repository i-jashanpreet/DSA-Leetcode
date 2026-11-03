class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        m = 0
        for i in nums:
            m+=abs(maxi-i)
        return m
        