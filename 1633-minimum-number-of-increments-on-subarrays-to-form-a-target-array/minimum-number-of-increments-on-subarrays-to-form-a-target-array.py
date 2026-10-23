class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        ans = target[0]
        for i in range(1,len(target)):
            if target[i-1]<target[i]:
                ans+=target[i]-target[i-1]
        return ans

        