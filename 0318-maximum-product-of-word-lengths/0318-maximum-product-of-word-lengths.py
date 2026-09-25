class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        masks = [0] * n
        for i in range(n):
            for ch in words[i]:
                masks[i] |= 1 << (ord(ch) - ord('a'))
        max_val = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return max_val