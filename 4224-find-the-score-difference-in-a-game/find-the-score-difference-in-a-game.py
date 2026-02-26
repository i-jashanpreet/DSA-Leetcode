class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        s1= 0
        s2 = 0
        act = 1
        for i in range(len(nums)):
            if nums[i]%2==1:
                if act==1:
                    act = 2
                else:
                    act = 1
            if (i+1)%6==0:
                if act==1:
                    act = 2
                else:
                    act = 1
            if act==1:
                s1+=nums[i]
            else:
                s2+=nums[i]
        return s1-s2