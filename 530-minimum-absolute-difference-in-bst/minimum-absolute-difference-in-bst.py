# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def f(node):
            if node == None:
                return
            arr.append(node.val)
            f(node.left)
            f(node.right)
        f(root)
        arr.sort()
        ans = float("inf")
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i - 1])
        return ans      