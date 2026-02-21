class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        conditions = [
            word == word.lower(),
            word == word.upper(),
            word == word.capitalize()
        ]
        return any(conditions)

        