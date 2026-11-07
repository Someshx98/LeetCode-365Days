import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        result = []
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        t = 0

        for j, dur in enumerate(tasks):
            t = max(t, j)

            while busy and busy[0][0] <= t:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            if not free:
                t = busy[0][0]
                while busy and busy[0][0] <= t:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            result.append(i)
            heapq.heappush(busy, (t + dur, w, i))

        return result