class Solution(object):
    def twoSum(self, nums, target):

        n = len(nums)
        freq = {}
        for i in range(0,n):
            need = target-nums[i]
            if need in freq:
                return [i,freq[need]]
            freq[nums[i]]=i
                
         



        
        