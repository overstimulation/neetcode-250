class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        res = -1
        for k, v in counts.items():
            if k == v and k > res:
                res = k
        return res
