class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        ans = 0
        spent = 0
        for actual, minimum in tasks:
            ans = max(ans, spent + minimum)
            spent += actual
        return ans
        