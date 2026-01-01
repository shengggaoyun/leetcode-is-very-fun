class Solution:
    """
    Intuition: Although finding the kth largest element, we use a 
        min heap of size k and we pop the root to maintain k size.

    Runtime:
        The push/pop operations take O(log k) time. We do this
        for each element in nums, so overall we have O(n log k).

        Instead of max heap, we are using a min heap,
        which reduces the size of the heap from n down to k.

    Memory:
        Heap bounded at size k, so O(k). 
        This is better than O(n) for max heap.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

        