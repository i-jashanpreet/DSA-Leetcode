class TrieNode:
    def __init__(self, idx):
        self.idx = idx
        self.children = [None] * 26
class Solution:
    def insertTrie(self, root, i, wordsContainer):
        word = wordsContainer[i]
        n = len(word)
        pCrawl = root
        for j in range(n - 1, -1, -1):
            ch_idx = ord(word[j]) - ord('a')
            if pCrawl.children[ch_idx] is None:
                pCrawl.children[ch_idx] = TrieNode(i)
            pCrawl = pCrawl.children[ch_idx]
            if len(wordsContainer[pCrawl.idx]) > n:
                pCrawl.idx = i
    def search(self, root, word):
        pCrawl = root
        result_idx = root.idx
        n = len(word)
        for i in range(n - 1, -1, -1):
            ch_idx = ord(word[i]) - ord('a')
            if pCrawl.children[ch_idx] is None:
                return result_idx
            pCrawl = pCrawl.children[ch_idx]
            result_idx = pCrawl.idx
        return result_idx
    def stringIndices(self, wordsContainer, wordsQuery):
        m = len(wordsContainer)
        n = len(wordsQuery)
        result = [0] * n
        root = TrieNode(0)
        for i in range(m):
            if len(wordsContainer[root.idx]) > len(wordsContainer[i]):
                root.idx = i
            self.insertTrie(root, i, wordsContainer)
        for i in range(n):
            result[i] = self.search(root, wordsQuery[i])
        return result