class Solution:
    """
        Intuition:
        every time we see an opening bracket, we push it onto the stack
        when we see a closing bracket, it must match the most recent opening bracket

        Runtime: O(n) we traverse the string exactly once
        each push and pop operation takes O(1) time

        Memory: O(n) we store every character of the input string on the stack
        """
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping.values(): #dictionary values
                stack.append(char)
            
            elif char in mapping:  #dictionary keys
                if not stack or stack.pop() != mapping[char]: #not stack true means len(stack) != 0
                    return False

        return not stack