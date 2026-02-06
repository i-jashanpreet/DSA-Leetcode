class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        a=[]
        b=[]
        c=[]
        for i in range(n):
            if nums[i]<pivot:
                a.append(nums[i])
            elif nums[i]==pivot:
                b.append(nums[i])
            else:
                c.append(nums[i])
        res = a+b+c
        return res        