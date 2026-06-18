class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        odd = [c for c in freq.values() if c % 2 != 0]
        even = [c for c in freq.values() if c % 2 == 0]

        return max(odd) - min(even)
