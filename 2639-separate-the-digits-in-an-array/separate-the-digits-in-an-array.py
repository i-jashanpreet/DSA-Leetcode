class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            n = len(str(i))
            if n == 1:
                ans.append(i)
            else:
                temp = []
                while i != 0:
                    ld = i % 10
                    temp.append(ld)
                    i = i // 10
                while temp:
                    ans.append(temp.pop())
        return ans

        