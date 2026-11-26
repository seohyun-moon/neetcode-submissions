# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def countLeft(Node):
            if not Node:
                return 0
            count = 1 + countLeft(Node.left) + countLeft(Node.right)
            return count
        
        left = 1 + countLeft(root.left)
        if k > left:
            return self.kthSmallest(root.right, k - left)
        if k < left:
            return self.kthSmallest(root.left, k)
        return root.val