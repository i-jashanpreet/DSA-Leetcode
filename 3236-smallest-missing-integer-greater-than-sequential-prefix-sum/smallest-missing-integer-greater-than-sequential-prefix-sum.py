class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i]-1 == nums[i-1]:
                s+=nums[i]
            else:
                break
        nums = set(nums)
        while s in nums:
            s+=1
        return s



        