class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        rem = {}
        for i in range(0,n):
            need = target-nums[i]
            if need in rem:
                return [i,rem[need]]
            rem[nums[i]]=i
                
         



        
        