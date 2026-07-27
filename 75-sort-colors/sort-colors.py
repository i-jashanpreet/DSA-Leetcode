class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1 = 0
        c2 = 0
        c3 = 0
        for i in nums:
            if i==0:
                c1+=1
            if i==1:
                c2+=1
            if i==2:
                c3+=1
        i = 0
        while c1:
            nums[i] = 0
            i+=1
            c1-=1
        while c2:
            nums[i] = 1
            i+=1
            c2-=1
        while c3:
            nums[i] = 2
            i+=1
            c3-=1
        
     