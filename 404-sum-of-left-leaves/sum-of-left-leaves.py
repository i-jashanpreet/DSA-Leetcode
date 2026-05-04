# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def f(root,isleft):
            if root==None:
                return
            if root.left==None and root.right==None and isleft==True:
                lst.append(root.val)
            f(root.left,True)
            f(root.right,False)
            return
        lst = []
        f(root,False)
        return sum(lst)
        