# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        sp = head
        fp = head
        prev = None
        i = 1
        while i<n:
            fp = fp.next
            i+=1
        if fp.next is None:
            return head.next
        while fp.next!=None:
            prev = sp
            sp = sp.next
            fp = fp.next
        prev.next = sp.next
        return head
        