import heapq

class KthLargest:
    """
     Intuition: We heapify the input list and delete all the elements until
     the size of heap is k, so we have the k largest elements.
     When inserting a new element, we push it onto the heap and but we pop the smallest
     element so the heap size is k. It's easier for retrieving the kth largest element,
     since we simply return the top element of the heap.

    Runtime:
        O(n log n) for building a heap

        O(log k) for inserting

        O(1) for retrieving the first element (heap[0])

    Memory:
        O(k) for the heap
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)