class Solution:
    """
    Intuition:
        Use 2 pointer approach to iterate through array.
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        ptr1 = 0
        ptr2 = n-1

        while ptr1 < ptr2:
            sum = numbers[ptr1] + numbers[ptr2]
            if sum == target:
                return [ptr1 + 1, ptr2 + 1]
            elif sum > target:
                ptr2 = ptr2 - 1
            elif (numbers[ptr1] + numbers[ptr2]) < target:
                ptr1 = ptr1 + 1
        return -1
       



        
        


        