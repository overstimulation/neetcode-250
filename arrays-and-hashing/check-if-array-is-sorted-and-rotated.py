class Solution:
    def check(self, nums: list[int]) -> bool:
        return sum(nums[i] > nums[(i + 1) % len(nums)] for i in range(len(nums))) <= 1
