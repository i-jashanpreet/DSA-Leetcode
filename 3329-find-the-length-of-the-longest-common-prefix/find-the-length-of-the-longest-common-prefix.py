class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pf = set()
        for i in arr1:
            i = str(i)
            temp = ""
            for j in i:
                temp+=j
                pf.add(temp)
        ans =0
        for i in arr2:
            i = str(i)
            temp =""
            for j in i:
                temp+=j
                if temp in pf:
                    ans = max(ans,len(temp))
        return ans

        