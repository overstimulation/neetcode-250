class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        n -= 1
        pos = 0
        while n > 0:
            if (x >> pos) & 1 == 0:
                res |= (n & 1) << pos
                n >>= 1
            pos += 1
        return res
