class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        s = sorted(freq, key=lambda x: freq[x], reverse=True)
        ans = ""
        for i in s:
            ans += i * freq[i]
        return ans
        