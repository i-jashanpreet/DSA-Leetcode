class Solution:
    def repairCars(self, ranks, cars: int) -> int:
        start = 1
        end = min(ranks) * cars * cars        
        while start < end:
            mid = (start + end) // 2          
            total = 0
            for r in ranks:
                total += int((mid // r) ** 0.5)          
            if total >= cars:
                end = mid
            else:
                start= mid + 1       
        return end

            