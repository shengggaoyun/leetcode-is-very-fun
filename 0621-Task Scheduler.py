from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = dict(Counter(tasks))
        max_heap = []
        for count in freq.values():
            heapq.heappush(max_heap, -count)
            
        Q = deque()
        time = 0

        while max_heap or Q:
            time = time + 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1

                if count < 0:
                    Q.append([count, time + n])
            
            if Q and Q[0][1] == time:
                heapq.heappush(max_heap, Q.popleft()[0])

        return time

            
        