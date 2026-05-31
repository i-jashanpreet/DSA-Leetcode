class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        valid = True
        for i in asteroids:
            if i<=mass:
                mass+=i
            else:
                valid = False
                break
        if valid:
            return True
        else:
            return False
                
        