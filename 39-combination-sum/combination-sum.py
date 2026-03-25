class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        # ans = []
        # def f(i,arr,target,ans,res):
        #     if i==len(arr):
        #         return 
        #     if target<0:
        #         return
        #     if target==0:
        #         ans.append(res)
        #         return
        #     res.append(arr[i])
        #     f(i+1,arr,target-arr[i],ans,res)
        #     f(i,arr,target-arr[i],ans,res)
        #     res.pop()
        #     f(i+1,arr,target,ans,res)
        # f(0,arr,target,ans,[])
        # return ans
        res = []
        def f(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if total>target or i>=len(arr):
                return
            curr.append(arr[i])
            f(i,curr,total+arr[i])
            curr.pop()
            f(i+1,curr,total)
        f(0,[],0)
        return res
        

