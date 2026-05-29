class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            new = str(i)
            sumi = 0
            for j in new:
                sumi+=int(j)
            arr.append(sumi)
        return min(arr)


        