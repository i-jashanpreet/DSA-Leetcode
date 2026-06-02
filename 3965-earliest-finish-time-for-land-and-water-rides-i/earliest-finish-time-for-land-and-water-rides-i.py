class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landFinish = landStartTime[i] + landDuration[i]
                waterStart = max(landFinish, waterStartTime[j])
                total1 = waterStart + waterDuration[j]
                waterFinish = waterStartTime[j] + waterDuration[j]
                landStart = max(waterFinish, landStartTime[i])
                total2 = landStart + landDuration[i]
                ans = min(ans, total1, total2)
        return ans
        