# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Intuition: srecursion

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

        