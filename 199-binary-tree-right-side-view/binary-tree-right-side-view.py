# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def f(node):
            if node==None:
                return []
            res =[]
            q = [node]
            while q:
                n = len(q)
                for i in range(n):
                    node = q.pop(0)
                    if i==n-1:
                        res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return res
        return f(root)



            


            


        