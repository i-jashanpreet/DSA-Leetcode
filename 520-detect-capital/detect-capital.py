class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        
        if word.lower() == word:
            return True
        
        if word[0].upper() == word[0]:
            for i in range(1, len(word)):
                if word[i].lower() != word[i]:
                    return False
            return True  
        
        return False
        