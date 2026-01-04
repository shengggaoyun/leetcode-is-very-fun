class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Intuition:
        An anagram means both strings have the exact same characters in the exact
        same quantities.By using two hash maps to count character frequencies, 
        we can then compare these maps to determine if the strings are anagrams.

        Runtime: O(n)

        Memory: O(1)
        Although we use Hash Maps, the space is capped by the size of the alphabet, so O(26).
        """
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # build frequency maps for both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT