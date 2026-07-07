class Solution:
    def minPartitions(self, n: str) -> int:
        m = 0
        for ch in n:
            m = max(m, int(ch))
        return m
        