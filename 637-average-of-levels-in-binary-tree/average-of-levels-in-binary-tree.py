# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return []
        ans = []
        q = deque([root])
        while q:
            l =[]
            for i in range(len(q)):
                e = q.popleft()
                l.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            ans.append(l)
        res = []
        for i in ans:
            sumi = sum(i)
            leni = len(i)
            avg = sumi/leni
            res.append(avg)
        return res

        