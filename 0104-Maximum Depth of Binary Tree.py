from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Intuition: recursion

    Runtime: O(n) every node visited exactly once to perform the swap

    Memory: O(log n) for balanced tree (root to leaf is height log n)
        O(n) for tree linked list shape due to recursion stack

    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        R, L = root.right, root.left

        Rdepth = self.maxDepth(R)
        Ldepth = self.maxDepth(L)

        return max(Rdepth, Ldepth) + 1


class Solution2:
    """
    Intuition: iterative, always keep track of the greatest depth

    Runtime: O(n) every node visited and added to the queue exactly once 

    Memory: O(n) process all the nodes

    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        Q = deque([(root, 1)])
        depth = 0

        while Q:
            node, currentDepth = Q.popleft()
            
            if currentDepth > depth:
                depth = currentDepth
            
            if node.left:
                Q.append([node.left, currentDepth + 1])
            
            if node.right:
                Q.append([node.right, currentDepth + 1])

        return depth
        

        