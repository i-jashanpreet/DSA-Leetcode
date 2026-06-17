# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        mx = 0
        res = []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= mx:
                mx = arr[i]
                res.append(arr[i])
        res.reverse()
        dummy = ListNode(0)
        cur = dummy
        for x in res:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next
        