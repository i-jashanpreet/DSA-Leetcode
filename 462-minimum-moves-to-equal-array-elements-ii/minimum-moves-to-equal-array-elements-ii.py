class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med_i = len(nums)//2
        med = nums[med_i]
        ans = 0
        for i in nums:
            ans+=abs(med-i)
        return ans
            