class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n  = len(nums)
        total = sum(nums)
        if total%2!=0:
            return False
        target = total//2
        memo = [[-1]*(target+1) for _ in range(n)]
        def f(i,target):
            if target==0:
                return True
            if i==0:
                if nums[0]==target:
                    return True
                else:
                    return False
            if memo[i][target]!=-1:
                return memo[i][target]
            if nums[i]<=target:
                take = f(i-1,target-nums[i])
            else:
                take = False
            not_take = f(i-1,target)
            res = take or not_take
            memo[i][target] = res
            return memo[i][target]
        return f(n-1,target)
        
        