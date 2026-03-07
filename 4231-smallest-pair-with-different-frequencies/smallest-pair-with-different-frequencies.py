class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        unique_nums = sorted(freq.keys())
        for i in range(len(unique_nums)):
            for j in range(i + 1, len(unique_nums)):
                x = unique_nums[i]
                y = unique_nums[j]

                if freq[x] != freq[y]:
                    return [x, y]
        return [-1, -1]