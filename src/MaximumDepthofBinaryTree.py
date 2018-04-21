# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MaximumDepthofBinaryTree:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        r_depth = self.maxDepth(root.right)
        l_depth = self.maxDepth(root.left)
        
        if r_depth > l_depth:
            return r_depth + 1
        
        return l_depth + 1