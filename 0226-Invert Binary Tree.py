from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Intuition: swap the left and right children for every node in the tree recursively

    Runtime: O(n) every node visited exactly once to perform the swap

    Memory: O(log n) for balanced tree (root to leaf is height log n)
        O(n) for tree linked list shape due to recursion stack

    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class Solution2:
    """
    Intuition: iterative

    Runtime: O(n) every node visited and added to the queue exactly once to perform the swap

    Memory: O(n) for the queue

    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        Q = deque([root])
        while Q:
            current = Q.popleft()

            current.left, current.right = current.right, current.left

            if current.left:
                Q.append(current.left)
            if current.right:
                Q.append(current.right)
                
        return root

        