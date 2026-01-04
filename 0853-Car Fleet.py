class Solution:
    """
    Intuition: 
        If a fast car is behind a slow car, it will eventually 
        catch up but will be forced to slow down and stay together as one fleet.
        If a car behind is slower than the car in front,
        it can never catch up and it becomes its own new fleet.

        If the time is greater than the current leader (stack[-1]), 
        it’s a new bottleneck so we push it onto the stack.
        
        If its time is less than or equal, it just merges to one fleet. 
        We decrement our fleet count.

        Runtime: O(n log n) for sorting the cars

        Memory: O(n) for the stack
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        fleet = n
        time = [0.0] * n
        stack = []

        for i, value in enumerate(position):
            time[i] = float((target - value)/speed[i])
            
        combined = [[pos, t] for pos, t in zip(position, time)]
        sorted_combined = sorted(combined, key=lambda pair: pair[0], reverse=True)

        for i in range(n):
            if not stack or (sorted_combined[i][1] > stack[-1][1]):
                stack.append(sorted_combined[i])
            else:
                fleet -= 1
        return fleet