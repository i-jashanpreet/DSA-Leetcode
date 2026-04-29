# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        temp = head
        prev = None
        while temp and temp.next:
            first = temp
            sec = first.next
            third = sec.next
            sec.next = first
            first.next = third
            if prev:
                prev.next = sec
            prev = first
            temp = third
        return new_head

        