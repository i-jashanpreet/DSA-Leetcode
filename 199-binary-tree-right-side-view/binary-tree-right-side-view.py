# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # def f(node):
        #     if node==None:
        #         return []
        #     res =[]
        #     q = [node]
        #     while q:
        #         n = len(q)
        #         for i in range(n):
        #             node = q.pop(0)
        #             if i==n-1:
        #                 res.append(node.val)
        #             if node.left:
        #                 q.append(node.left)
        #             if node.right:
        #                 q.append(node.right)
        #     return res
        # return f(root)
        ans = []
        def rev_post_order(node,level):
            if node==None:
                return
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                rev_post_order(node.right,level+1)
            if node.left:
                rev_post_order(node.left,level+1)
        rev_post_order(root,0)
        return ans




            


            


        