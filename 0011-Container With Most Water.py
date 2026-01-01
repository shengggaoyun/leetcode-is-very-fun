class Solution:
    """
    Intuition:
        We are limited by the height of the shorter line, so we move the pointer
        with shorter height closer, hoping to reach a taller height that increases the area.

    Runtime: O(n)

    Memory: O(1) for only storing pointers.
    """
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1

        amount = 0
        while left < right:
            width = right - left
            maxHeight = min(height[left], height[right])

            if width * maxHeight > amount:
                amount = width * maxHeight

            if height[left] < height[right]:
                left = left + 1
        
            else:
                right = right - 1
                
        return amount