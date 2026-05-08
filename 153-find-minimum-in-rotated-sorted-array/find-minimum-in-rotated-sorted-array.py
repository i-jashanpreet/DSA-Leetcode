class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        st = 0
        end = n-1
        mini = 10**18
        while st<=end:
            mid = (st+end)//2
            mini = min(mini,nums[mid])
            if nums[end]<nums[st] and nums[end]<nums[mid]:
                st = mid+1
            else:
                end = mid-1
        return mini


        