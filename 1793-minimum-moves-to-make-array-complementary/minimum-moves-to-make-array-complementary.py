class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        pairs = n // 2
        moves = 2 * pairs
        for i in range(pairs):
            a = nums[i]
            b = nums[n - 1 - i]
            low = min(a, b)
            high = max(a, b)
            total = a + b
            diff[low + 1] -= 1
            diff[high + limit + 1] += 1
            diff[total] -= 1
            diff[total + 1] +=1
        ans = float("inf")
        curr = moves
        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)
        return ans
        