from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(k: int) -> int:
            count = defaultdict(int)
            res = l = 0
            for r in range(len(nums)):
                count[nums[r]] += 1
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += r - l + 1
            return res

        return atMost(k) - atMost(k - 1)
