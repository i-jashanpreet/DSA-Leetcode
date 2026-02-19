class Solution:
    def repairCars(self, ranks, cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars   # maximum possible time      
        while left < right:
            mid = (left + right) // 2          
            total = 0
            for r in ranks:
                total += int((mid // r) ** 0.5)          
            if total >= cars:
                right = mid
            else:
                left = mid + 1       
        return left

            