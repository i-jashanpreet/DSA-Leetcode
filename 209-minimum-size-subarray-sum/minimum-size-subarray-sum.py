class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        s = 0
        ans = float("inf")
        while j < len(nums):
            s += nums[j]

            while s >= target:
                ans = min(ans, j - i + 1)
                s -= nums[i]
                i += 1

            j += 1
        if ans==float("inf"):
            return 0
        return ans           






        