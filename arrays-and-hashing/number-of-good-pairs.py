class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counts = {}
        res = 0
        for num in nums:
            res += counts.get(num, 0)
            counts[num] = counts.get(num, 0) + 1
        return res