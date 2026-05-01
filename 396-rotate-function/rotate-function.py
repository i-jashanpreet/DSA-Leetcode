class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n =len(nums)
        s = sum(nums)
        f = 0
        for i in range(n):
            f+=i*nums[i]
        max_val = f
        for k in range(1,n):
            f+=s-n*nums[n-k]
            max_val = max(f,max_val)
        return max_val