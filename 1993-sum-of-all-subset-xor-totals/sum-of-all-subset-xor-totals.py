class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def f(i,currxor):
            if i==len(nums):
                return currxor
            take = f(i+1,currxor^nums[i])
            nottake = f(i+1,currxor)
            return take+nottake
        return f(0,0)        