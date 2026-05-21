class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = 0
        max_sum = float("-inf")
        cur_max = 0
        min_sum = float("inf")
        cur_min = 0

        for x in nums:
            total += x
            cur_max = max(cur_max + x, x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + x, x)
            min_sum = min(min_sum, cur_min)

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
