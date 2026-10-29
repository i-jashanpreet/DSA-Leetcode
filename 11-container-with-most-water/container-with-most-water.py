class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_v = 0
        while l < r:
            width = r - l
            h = min(height[l], height[r])
            max_v = max(max_v, width * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_v
        