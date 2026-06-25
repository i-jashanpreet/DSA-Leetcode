class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            c = 0
            
            for j in range(i, n):
                if nums[j] == target:
                    c += 1
                
                ln = j - i + 1
                
                if c > ln // 2:
                    ans += 1
        
        return ans