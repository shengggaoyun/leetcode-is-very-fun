class Solution:

    """
    Intuition: Question: Given temperature array, return an array where res[i] 
    is the days needed to wait to get a higher temperature

    Solution:
    For loop, if current temp is smaller than top of stack, append its index to stack.
    If current temp is bigger, then set res[stack.pop()] = i - popped value
    Ex: [3, 1, 2, 4]: Basically, keep going down until the previous number is smaller 
    (1, 2 pair, currently at  2). Now we know the answer of temp = 1: res[index of 1] = index of 2 - index of 1. 
    Now 1 is popped from stack, stack contains (3, 2). Next we reach 4, 
    see previous number is smaller (2, 4 pair, currently at 4). 2 popped from stack: (stack is now (3)) 
    we record the answer of temp = 2 in the res array. 
    Btw once we are in an iteration in the for loop we keep checking if the current number is bigger than the previous (top of stack). 
    Now (3 4 pair, currently at 4), record the answer of temp = 3 which is index of 4 - index of 3


    Runtime: O(n)

    Memory: O(n)

    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):  #up to -1 to include index 0

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack: #difference between warm day and now
                result[i] = stack[-1] - i
            
            stack.append(i) #last day index always on stack at first if empty
        
        return result
        





        