import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        Intuition: push all integers on the stack. if we have an operand, we
        pop two numbers from the stack and perform the operation.

        Runtime: O(n)

        Memory: O(n)
        """
        n = len(tokens)
        stack = []
        
        for i in range(n):
            if tokens[i] in "+-*/":
                operation = tokens[i]
                arg2 = stack.pop()
                arg1 = stack.pop()

                if operation == '+':
                    result = arg1 + arg2
                elif operation == '-':
                    result = arg1 - arg2
                elif operation == '*':
                    result = arg1 * arg2
                elif operation == '/':
                    result = float(arg1) / arg2
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                
                stack.append(int(result))
            else:
                # Token is a number, push it onto the stack
                stack.append(int(tokens[i]))

        return stack[0]