class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        i = 0  
        radius = 0
        
        for house in houses:
            while (i + 1 < len(heaters) and 
                   abs(heaters[i + 1] - house) <= abs(heaters[i] - house)):
                i += 1
            radius = max(radius, abs(heaters[i] - house))
        return radius

        