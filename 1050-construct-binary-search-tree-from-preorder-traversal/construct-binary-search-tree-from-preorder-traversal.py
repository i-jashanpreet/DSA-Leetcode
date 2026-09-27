# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        def f(i, j):
            if i > j:
                return None
            root = TreeNode(preorder[i])
            k = i + 1
            while k <= j and preorder[k] < preorder[i]:
                k += 1
            root.left = f(i + 1, k - 1)
            root.right = f(k, j)
            return root
        return f(0, len(preorder) - 1)        