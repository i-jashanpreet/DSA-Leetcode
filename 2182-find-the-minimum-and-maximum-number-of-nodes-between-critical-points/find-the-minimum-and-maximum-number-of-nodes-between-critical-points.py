# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos = []
        idx = 1
        prev = head
        cur = head.next
        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                pos.append(idx)
            prev = cur
            cur = cur.next
            idx += 1
        if len(pos) < 2:
            return [-1, -1]
        mn = float('inf')
        for i in range(1, len(pos)):
            mn = min(mn, pos[i] - pos[i - 1])
        mx = pos[-1] - pos[0]
        return [mn, mx]     