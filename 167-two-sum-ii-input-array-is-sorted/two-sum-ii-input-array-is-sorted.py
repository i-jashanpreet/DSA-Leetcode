class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        n = len(nums)
        r = n-1
        ans = []
        while l<r:
            sumi = nums[l]+nums[r]
            if sumi==target:
                ans.append(l+1)
                ans.append(r+1)
                return ans
            elif sumi>target:
                r = r-1
            else:
                l = l+1
        

        
        