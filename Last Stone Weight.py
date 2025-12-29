import heapq

class Solution:
    """
    Intuition:
        build a min heap, then -1 * all elements, so it becomes a max heap.
        -1 * first element is the biggest element in the heap

    Runtime: 
        building the heap and heapify each take O(n) 
        pop/push operation takes O(log n)
        each  iteration of the loop reduces the size of the heap
        by at least one. so O(n) in the worst case where at the end
        there is no stone left

    Memory: O(n) for stones heap

    """
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []
        for stone in stones:
            stone = -stone
            heapq.heappush(max_heap, stone)

        while len(max_heap) >= 1:

            if len(max_heap) > 1:
                heaviest1 = -1 * heapq.heappop(max_heap)
                heaviest2 = -1 * heapq.heappop(max_heap)

                if heaviest1 != heaviest2:
                    newWeight = -1 * (heaviest1 - heaviest2)
                    heapq.heappush(max_heap, newWeight)

            else:
                return -1 * max_heap[0]

        return 0




        



        