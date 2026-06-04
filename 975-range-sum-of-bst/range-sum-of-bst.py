# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        def f(node):
            if node==None:
                return
            arr.append(node.val)
            f(node.left)
            f(node.right)
        f(root)
        sumi = 0
        for i in arr:
            if i>=low and i<=high :
                sumi+=i
        return sumi

