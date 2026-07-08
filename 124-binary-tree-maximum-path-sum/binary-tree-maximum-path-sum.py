# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans =float("-inf")
        def f(node):
            nonlocal ans
            if node==None:
                return 0
            l = max(0, f(node.left))
            r = max(0, f(node.right))
            ans = max(ans,l+r+node.val)
            return node.val+max(l,r)
        f(root)
        return ans



     