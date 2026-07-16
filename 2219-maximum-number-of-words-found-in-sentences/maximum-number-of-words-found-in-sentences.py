class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        for i in sentences:
            s =0
            for j in i:
                if j==" ":
                    s+=1
            ans.append(s)
        return max(ans)+1


        