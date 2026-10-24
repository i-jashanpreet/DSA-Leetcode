class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,arriveBob: str, leaveBob: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        def convert(date):
            m, d = map(int, date.split("-"))
            return sum(days[:m-1]) + d
        a = convert(arriveAlice)
        b = convert(leaveAlice)
        c = convert(arriveBob)
        d = convert(leaveBob)
        return max(0, min(b, d) - max(a, c) + 1)
