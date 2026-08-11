class Solution:
    def check(self, nums: List[int]) -> bool:
        c =0
        n = len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                c+=1
        if nums[-1]>nums[0]:
            c+=1
        if c>1:
            return False
        else:
            return True
        