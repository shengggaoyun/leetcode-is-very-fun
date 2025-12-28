class Solution:
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