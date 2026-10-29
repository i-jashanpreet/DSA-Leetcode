class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        ans = []
        for slot in intervals:
            if not ans or ans[-1][1]<slot[0]:
                ans.append(slot)
            else:
                ans[-1][1] = max(ans[-1][1], slot[1])
        return ans




        