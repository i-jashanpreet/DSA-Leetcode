# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr =[]
        def fs(node):
            if node == None:
                return
            arr.append(node.val)
            fs(node.left)
            fs(node.right)
        fs(root)
        f = {}
        for i in arr:
            f[i] = f.get(i, 0) + 1
        mx = max(f.values())
        ans = []
        for j in f:
            if f[j] == mx:
                ans.append(j)
        return ans

            
        