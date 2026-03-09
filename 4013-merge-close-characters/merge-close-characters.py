class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        s = list(s)   
        while True:
            merged = False      
            for i in range(len(s)):
                for j in range(i + 1, min(i + k + 1, len(s))):   
                    if s[i] == s[j]:
                        s.pop(j)   
                        merged = True
                        break
                if merged:
                    break
            if not merged:
                break
        return "".join(s)