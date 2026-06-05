from functools import lru_cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve(x):
            if x < 0:
                return 0
            s = str(x)
            @lru_cache(None)
            def dp(pos, tight, started, prev1, prev2):
                if pos == len(s):
                    return (1, 0)
                limit = int(s[pos]) if tight else 9
                totalWays = 0
                totalWave = 0
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    if not started and d == 0:
                        ways, wave = dp(pos + 1,ntight,False,-1,-1)
                        totalWays += ways
                        totalWave += wave
                    else:
                        add = 0
                        if prev2 != -1:
                            if ((prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d)):
                                add = 1
                        ways, wave = dp(pos + 1,ntight,True,d,prev1)
                        totalWays += ways
                        totalWave += wave + add * ways
                return (totalWays, totalWave)
            return dp(0, True, False, -1, -1)[1]
        return solve(num2) - solve(num1 - 1)

                
        