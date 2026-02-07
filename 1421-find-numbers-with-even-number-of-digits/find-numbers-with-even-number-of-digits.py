class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            no_ld = 0
            while i!=0:
                ld = i%10
                i=i//10
                no_ld+=1
            if no_ld%2==0:
                c+=1
        return c

        