class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced = 0

        for fruit in fruits:
            for i in range(len(baskets)):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    break
            else:
                unplaced += 1

        return unplaced




        