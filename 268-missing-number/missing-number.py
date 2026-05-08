class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # total = n * (n + 1) // 2
        # return total - sum(nums)
        nums.sort()
        n = len(nums)
        st = 0
        end = len(nums)-1
        while st<=end:
            mid = (st+end)//2
            if nums[mid]==mid:
                st = mid+1
            else:
                end = mid-1
        return st

        