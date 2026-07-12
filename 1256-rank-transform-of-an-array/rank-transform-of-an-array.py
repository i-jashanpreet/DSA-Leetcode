class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(arr)
        d = {}
        r = 1
        for x in s:
            if x not in d:
                d[x] = r
                r += 1
        ans = []
        for x in arr:
            ans.append(d[x])
        return ans     