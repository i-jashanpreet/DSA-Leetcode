# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def f(node, arr):
            if node == None:
                return
            if node.left == None and node.right == None:
                arr.append(node.val)
            f(node.left, arr)
            f(node.right, arr)
        ans1 = []
        ans2 = []
        f(root1, ans1)
        f(root2, ans2)
        return ans1 == ans2
        