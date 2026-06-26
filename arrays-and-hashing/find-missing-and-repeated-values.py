class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        count = [0] * (n * n + 1)
        for row in grid:
            for num in row:
                count[num] += 1
        a = b = 0
        for i in range(1, n * n + 1):
            if count[i] == 2:
                a = i
            elif count[i] == 0:
                b = i
        return [a, b]