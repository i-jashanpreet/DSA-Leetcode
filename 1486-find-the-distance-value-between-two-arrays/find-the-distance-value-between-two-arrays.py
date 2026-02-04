class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0

        for x in arr1:
            start = 0
            end = len(arr2) - 1
            found = False

            while start <= end:
                mid = (start + end) // 2

                if abs(arr2[mid] - x) <= d:
                    found = True
                    break
                elif arr2[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1

            if not found:
                count += 1

        return count

        