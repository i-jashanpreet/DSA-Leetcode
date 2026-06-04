# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def f(node):
            if node==None:
                return
            arr.append(node.val)
            f(node.left)
            f(node.right)
        f(root)
        ans = arr[0]
        for i in arr:
            if i!=ans:
                return False
        return True