class Solution:
    """
    Intuition:
        We can reduce the problem to a 2Sum problem by fixing a first element:
        -element 1 = element 2 + element 3

        By sorting the array, we reduce the iterations since if we arrive to a first element
        greater than 0 that we already exhaust all the triplets possible.

        We iterate through the sorted array and use a 2 pointer approach to solve
        for 2Sum to find the 2 remaining elements to form a valid triplet.

        ***How to prevent duplicates

    Runtime: O(n^2)

    Memory: O(n) to store result. O(1) for only storing pointers.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            ptr1 = i + 1
            ptr2 = n - 1

            while ptr1 < ptr2:
                sum = nums[ptr1] + nums[ptr2]
                if sum == target:
                    output.append([nums[i], nums[ptr1], nums[ptr2]])

                    # skip duplicates for the left and right pointer
                    while ptr1 < ptr2 and nums[ptr1] == nums[ptr1 + 1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums[ptr2] == nums[ptr2 - 1]:
                        ptr2 -= 1

                    ptr1 = ptr1 + 1
                    ptr2 = ptr2 - 1

                elif sum > target:
                    ptr2 = ptr2 - 1
                elif (nums[ptr1] + nums[ptr2]) < target:
                    ptr1 = ptr1 + 1
        return output


        