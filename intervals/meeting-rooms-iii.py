import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available = list(range(n))
        occupied = []
        count = [0] * n

        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                heapq.heappush(available, heapq.heappop(occupied)[1])

            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                time, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (time + end - start, room))

            count[room] += 1

        return count.index(max(count))
