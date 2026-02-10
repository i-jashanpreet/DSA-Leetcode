# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         start = 0
#         end = n-1
#         ans = -1
#         while start<=end:
#             mid = (start+end)//2
#             if nums[mid]==mid:
#                 ans = nums[mid]
#                 end = mid-1
#             else:
#                 start = mid+1
#         return ans

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()   # modifies array (constraint broken, but allowed here)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]



        