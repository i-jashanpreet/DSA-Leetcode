class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
        ans = ""
        for i in arr:
            ans+=str(i)
        new = str(int(ans)+1)
        res = []
        for i in new:
            res.append(int(i))
        return res


        