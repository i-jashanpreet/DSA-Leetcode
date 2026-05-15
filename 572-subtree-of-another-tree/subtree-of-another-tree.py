# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a,b):
            if a==None and b==None:
                return True
            if a==None or b==None:
                return False
            if a.val!=b.val:
                return False
            l = same(a.left,b.left)
            r = same(a.right,b.right)
            return l and r
        def f(node):
            if node==None:
                return False
            if same(node,subRoot):
                return True
            return f(node.left) or f(node.right)
        return f(root)