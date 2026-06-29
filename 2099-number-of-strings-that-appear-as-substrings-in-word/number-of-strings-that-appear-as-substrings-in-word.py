class Solution:
    def numOfStrings(self, p: List[str], word: str) -> int:
        c = 0
        for i in p:
            if i in word:
                c+=1
        return c
        