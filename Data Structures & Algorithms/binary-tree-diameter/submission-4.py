# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #making instance of the class to make it accessible inside the nested fuction
        self.best = 0

        def height(root):
            if not root:
                return False
            left = height(root.left)
            right = height(root.right)

            self.best = max(self.best, left + right)
            return 1 + max(left, right)
        
        height(root)
        return self.best
            
