class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        new = nums[::-1]
        arr =nums+new
        return arr