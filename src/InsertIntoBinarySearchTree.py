# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def recursive_traverse(root: TreeNode, val: int):
            
            if val <= root.val:
                if root.left != None:
                    recursive_traverse(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right != None:
                    recursive_traverse(root.right, val)
                else:
                    root.right = TreeNode(val)
            
        recursive_traverse(root, val)
        
        return root
