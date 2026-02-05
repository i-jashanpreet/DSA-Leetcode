class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        prefix = []
        total = 0
        for x in nums:
            total += x
            prefix.append(total)

        ans = []

        for q in queries:
            count = 0
            for s in prefix:
                if s <= q:
                    count += 1
                else:
                    break
            ans.append(count)

        return ans

        