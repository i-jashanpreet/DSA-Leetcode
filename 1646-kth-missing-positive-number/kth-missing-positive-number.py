class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss = []
        current = 1
        i = 0
        n = len(arr)
        while len(miss) < k:
            if i < n and arr[i] == current:
                i += 1
            else:
                miss.append(current)
            current += 1

        return miss[k - 1]




        