class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = []
        ans = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        i = 0
        j = len(ans) - 1
        while i < j:
            total = ans[i] + ans[j]
            if total == k:
                return True
            elif total < k:
                i += 1
            else:
                j -= 1
        return False





        