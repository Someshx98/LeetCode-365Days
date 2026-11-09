import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, s = heapq.heappop(busy)
                free.add(s)

            if not free:
                continue

            idx = free.bisect_left(i % k)
            if idx == len(free):
                idx = 0
            s = free.pop(idx)

            count[s] += 1
            heapq.heappush(busy, (start + dur, s))

        best = max(count)
        return [i for i, c in enumerate(count) if c == best]