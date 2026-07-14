# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        res = []
        q = deque([root])
        while q:
            l = []
            for i in range(len(q)):
                e = q.popleft()
                l.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            res.append(l)
        res.reverse()
        return res


        