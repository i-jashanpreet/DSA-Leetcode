class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour%12)*30+minutes*0.5
        m = minutes*6
        ans = abs(h-m)
        final = min(ans,360-ans)
        return final
        