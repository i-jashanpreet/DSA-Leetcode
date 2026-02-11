class Solution:
    def maxDistance(self, position, m):
        position.sort()

        # Check if we can place m balls with minimum distance 'dist'
        def canPlace(dist):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= dist:
                    count += 1
                    last = position[i]
                if count == m:
                    return True

            return False

        start = 1
        end = position[-1] - position[0]
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if canPlace(mid):
                ans = mid
                start = mid + 1   # try bigger distance
            else:
                end = mid - 1     # try smaller distance

        return ans


        