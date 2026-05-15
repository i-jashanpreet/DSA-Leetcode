# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:   
    def lowestCommonAncestor(self, root, p, q):       
        def solve(node, p, q):            
            if node == None:
                return None            
            if node == p or node == q:
                return node            
            l = solve(node.left, p, q)
            r = solve(node.right, p, q)           
            if l == None and r == None:
                return None  
            elif l == None:
                return r          
            elif r == None:
                return l           
            else:
                return node
        return solve(root, p, q)
        