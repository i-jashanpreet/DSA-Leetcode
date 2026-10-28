import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        sumi = sum(nums)
        target = sumi / 2
        new_sum = 0
        ans = 0
        while new_sum < target:
            x = -heapq.heappop(heap)
            half = x / 2
            new_sum += half
            heapq.heappush(heap, -half)
            ans += 1
        return ans



        