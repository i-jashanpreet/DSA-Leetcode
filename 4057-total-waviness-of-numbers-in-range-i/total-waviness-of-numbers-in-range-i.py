class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        w = 0
        for i in range(num1,num2+1):
            i = str(i)
            for j in range(1,len(i)-1):
                if (i[j]<i[j+1] and i[j]<i[j-1]) or (i[j]>i[j+1] and i[j]>i[j-1]):
                    w+=1
        return w

                
        