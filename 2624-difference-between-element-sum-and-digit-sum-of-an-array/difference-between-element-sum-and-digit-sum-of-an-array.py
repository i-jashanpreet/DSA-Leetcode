class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        gs = 0
        for i in nums:
            sumi=0
            while i>0:
                ld = i%10
                sumi+=ld
                i=i//10
            gs+=sumi
        return abs(gs-s)
    
            

            


        