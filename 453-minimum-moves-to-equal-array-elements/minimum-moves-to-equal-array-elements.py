class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        m = 0
        for i in nums:
            m += i - mini
        return m


