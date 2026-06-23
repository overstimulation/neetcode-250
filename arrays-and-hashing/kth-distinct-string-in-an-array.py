class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = {}
        for s in arr:
            counts[s] = counts.get(s, 0) + 1
        
        distinct_count = 0
        for s in arr:
            if counts[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        return ""