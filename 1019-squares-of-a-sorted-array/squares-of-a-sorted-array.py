class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        ans = [0]*n
        k = n-1
        while i<=j:
            i_sq = nums[i]*nums[i]
            j_sq = nums[j]*nums[j]
            if j_sq>=i_sq:
                ans[k] = j_sq
                j = j-1
            else:
                ans[k] = i_sq
                i = i+1
            k = k-1
        return ans


        