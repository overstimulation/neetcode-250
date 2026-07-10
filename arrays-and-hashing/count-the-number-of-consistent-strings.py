class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        res = 0
        for word in words:
            for char in word:
                if char not in allowed_set:
                    break
            else:
                res += 1
        return res