import heapq
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        heap = []
        events.sort()
        day = events[0][0]
        i = 0
        ans = 0
        while len(heap) or i < n:
            while i < n and day == events[i][0]:
                heapq.heappush(heap, events[i][1])
                i += 1
            while len(heap) and heap[0] < day:
                heapq.heappop(heap)

            if len(heap):
                heapq.heappop(heap)
                ans += 1

            day += 1

        return ans