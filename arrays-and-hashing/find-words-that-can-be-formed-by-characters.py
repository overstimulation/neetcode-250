from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_counts = Counter(chars)
        res = 0
        for word in words:
            word_counts = Counter(word)
            if all(word_counts[c] <= char_counts[c] for c in word_counts):
                res += len(word)
        return res
