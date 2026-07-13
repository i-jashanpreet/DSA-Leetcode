# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            l = []
            for i in range(n):
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(l)
        m = len(ans)
        for i in range(m):
            if i%2==1:
                ans[i].reverse()
        return ans


        