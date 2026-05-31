# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def f(node, path, total):
            if not node:
                return
            path.append(node.val)
            total += node.val
            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(path[:])
            f(node.left, path, total)
            f(node.right, path, total)
            path.pop() 
        f(root, [], 0)
        return ans
        