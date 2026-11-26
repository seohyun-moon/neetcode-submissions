# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def countLeftNodes (root:TreeNode, count: int, max: int) -> int:
            if not root.left:
                return count
            if root.left.val < max:
                root = root.left
                return countLeftNodes(root, count, max) + countRightNodes(root, 0, max)
            else:
                root = root.left
                max = root.val
                count += 1
                return countLeftNodes(root, count, max) + countRightNodes(root, 0, max)

        def countRightNodes (root:TreeNode, count: int, max: int) -> int:
            if not root.right:
                return count
            if root.right.val < max:
                root = root.right
                return countRightNodes(root, count, max) + countLeftNodes(root, 0, max)
            else:
                root = root.right
                max = root.val
                count += 1
                return countRightNodes(root, count, max) + countLeftNodes(root, 0, max)

        if not root:
            return 0
        else:
            return countRightNodes(root, 0, root.val) + countLeftNodes(root, 0, root.val) + 1