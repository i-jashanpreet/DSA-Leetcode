from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        arr = []

        for i in range(n):
            sum_i = 0
            for k in str(nums[i]):
                sum_i += int(k)
            arr.append((sum_i, nums[i]))
        target = sorted(arr)
        pos = {arr[i]: i for i in range(n)}
        for i in range(n):
            if arr[i] != target[i]:
                j = pos[target[i]]

                pos[arr[i]] = j
                pos[arr[j]] = i

                arr[i], arr[j] = arr[j], arr[i]
                c += 1

        return c

            
            


        