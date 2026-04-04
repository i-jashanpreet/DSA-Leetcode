class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(i,seq):
            if i>=len(nums):
                res.append(seq)
                return
            f(i+1,seq+[nums[i]])
            f(i+1,seq)
        f(0,[])
        return res
            

        