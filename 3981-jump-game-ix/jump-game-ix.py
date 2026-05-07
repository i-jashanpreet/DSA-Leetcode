class Solution:
    def maxValue(self, nums):
        n = len(nums)
        ans = [0] * n
        stack = []
        for i in range(n):
            curr_val = nums[i]
            curr_left = i
            curr_right = i
            while stack and stack[-1][0] > nums[i]:
                top = stack.pop()

                curr_val = max(curr_val, top[0])

                curr_left = top[1]

            stack.append([curr_val, curr_left, curr_right])

        for comp in stack:

            for j in range(comp[1], comp[2] + 1):

                ans[j] = comp[0]

        return ans