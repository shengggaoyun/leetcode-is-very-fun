class Solution:
    """
    Intuition: 
    use a hash set to store elements as we iterate through the array 
    because it allows O(1) for adding and searching

    Runtime: O(n) to traverse the list exactly once 
    and each lookup and insertion in the set is O(1)

    Memory: O(n) worst case no duplicates, we must store every element
    in the input to the hash set
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False