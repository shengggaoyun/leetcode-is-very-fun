class Solution:
    """
    Intuition:
        Use 2 pointer approach to iterate through string, one starting from the left
        and another from the right.
        
    Runtime: O(n)

    Memory: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        phrase = ''
        for char in s:
            if ('a' <= char <= 'z') or ('0' <= char <= '9'):
                phrase = phrase + char

        n = len(phrase)
        left = 0
        right = n-1

        while left < right:
            if phrase[left] != phrase[right]:
                return False
            left = left + 1
            right = right - 1

        return True

class Solution2:
    """
    Use Python built-in functions
    """

    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s.lower() if char.isalnum())
        return s == s[::-1]



        
        