class Solution:
    """
    Intuition: for every element in the array, we are looking for its complement
    we can store all the complements in a hash map as we iterate through the array
    if we find the complement in the hash map, we return the indices

    Runtime: O(n)

    Memory: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            req = target - nums[i]
            if req in hashmap:
                return [hashmap[req], i]
            hashmap[nums[i]] = i
        