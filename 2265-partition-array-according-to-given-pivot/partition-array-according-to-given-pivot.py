class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        # a=[]
        # b=[]
        # c=[]
        # for i in range(n):
        #     if nums[i]<pivot:
        #         a.append(nums[i])
        #     elif nums[i]==pivot:
        #         b.append(nums[i])
        #     else:
        #         c.append(nums[i])
        # res = a+b+c
        # return res        
        cl=0
        ce=0
        cm=0
        for i in nums:
            if i<pivot:
                cl+=1
            elif i==pivot:
                ce+=1
            else:
                cm+=1
        i=0
        j=cl
        k=n-cm
        new=[0]*n
        for h in nums:
            if h<pivot:
                new[i]=h
                i+=1
            elif h==pivot:
                new[j]=h
                j+=1
            else:
                new[k]=h
                k+=1
        return new
