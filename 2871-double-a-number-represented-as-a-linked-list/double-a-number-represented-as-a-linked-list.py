# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >= 5:
            newHead = ListNode(0)
            newHead.next = head
            head = newHead
        curr = head
        while curr:
            curr.val = (curr.val * 2) % 10
            if curr.next and curr.next.val >= 5:
                curr.val += 1
            curr = curr.next
        return head






        