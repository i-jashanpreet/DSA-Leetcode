# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sp = head
        fp = head
        i = 1
        while i<k:
            fp = fp.next
            i+=1
        kth_node_start = fp
        while fp.next!=None:
            sp = sp.next
            fp = fp.next
        kth_node_end = sp
        t = kth_node_start.val
        kth_node_start.val = kth_node_end.val
        kth_node_end.val = t
        return head



        