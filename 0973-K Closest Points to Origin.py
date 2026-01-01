class Solution:
    """
    Runtime: Building the heap is O(n log n), then we extract the k smallest elements,
    k pop operations take O(log n) each, so overall O(n log n + k log n) time.
    => O(n log n) time

    Memory: O(N) for the heap because we are not evicting anything,
    the size of the heap keeps growing until all points are processed.

    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []
        for coordinate in points:
            x, y = coordinate[0], coordinate[1]
            heapq.heappush(min_heap, (x**2 + y**2, coordinate))
        
        for _ in range(k):
            distance, coordinate = heapq.heappop(min_heap)
            result.append(coordinate)
        return result
    
"""
MORE OPTIMAL SOLUTION BY USING MAX HEAP
"""
class Solution2:
    """
    Intuition: Although we want the kth closest one, we use
    a max heap to track the distance. In the max heap, 
    the point with the highest distance will be at the root.
    Thus, if we need to evict, we simply just pop the root.

    Runtime: Each point processed once, push/pop operations take
    O(log k) since the heap size is at most k.
    Overall O(n log k) time.
    
    Since k < n, it's more advantageous if we can
    apply the log factor on n instead of k.

    Memory: O(k) for the heap because we only store k + 1 elements
    in the memory at any moment.

    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for coordinate in points:
            x, y = coordinate[0], coordinate[1]
            value = -(x**2 + y**2)
            heapq.heappush(max_heap, (value, coordinate))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [item[1] for item in max_heap]

