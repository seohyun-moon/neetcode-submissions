# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []

        if root == None:
            return res
        else:
            queue.append(root)

        while len(queue) > 0:
            lvl = []
            for i in range(len(queue)):
                curr = queue.popleft()
                lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lvl[len(lvl)-1])
        return res