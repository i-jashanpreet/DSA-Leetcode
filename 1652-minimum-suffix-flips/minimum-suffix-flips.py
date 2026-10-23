class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        prev = "0"
        for i in target:
            if i!=prev:
                ans+=1
                prev = i
        return ans
        