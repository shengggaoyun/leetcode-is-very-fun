# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Intuition: the diameter of a given node is the sum of depth 
            in left and right subtrees (it is also the longest path from two nodes)

    *** iterative approach ?

    Runtime: O(n) every node visited exactly once

    Memory: O(log n) for balanced tree (root to leaf is height log n)
        O(n) for tree linked list shape due to recursion stack

    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def maxDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
          
            Rdepth = maxDepth(node.right)
            Ldepth = maxDepth(node.left)

            self.diameter = max(self.diameter, Rdepth + Ldepth)

            return max(Rdepth, Ldepth) + 1

        maxDepth(root)
        return self.diameter