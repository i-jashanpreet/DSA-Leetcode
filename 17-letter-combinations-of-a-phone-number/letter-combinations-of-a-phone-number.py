class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        D = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]}
        arr = []
        def f(i,ans):
            if i==len(digits):
                arr.append(ans)
                return
            for ch in D[digits[i]]:
                f(i+1,ans+ch)
        f(0,"")
        return arr

        