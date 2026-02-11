class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def canPlace(dist):
            count = 1
            last = position[0]

            for pos in position[1:]:
                if pos - last >= dist:
                    count += 1
                    last = pos
                    if count == m:
                        return True
            return False

        left = 1
        right = position[-1] - position[0]

        while left < right:
            mid = (left + right + 1) // 2  # bias to the right

            if canPlace(mid):
                left = mid       # try bigger distance
            else:
                right = mid - 1  # reduce distance

        return left


        