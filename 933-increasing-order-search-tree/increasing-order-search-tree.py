# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def f(node):
            if node==None:
                return
            f(node.left)
            arr.append(node.val)
            f(node.right)
        f(root)
        newroot= TreeNode(arr[0])
        temp = newroot
        for i in range(1,len(arr)):
            temp.right = TreeNode(arr[i])
            temp = temp.right
        return newroot