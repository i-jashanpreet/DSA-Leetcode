# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        dummy = ListNode(0)
        curr = dummy
        sumi = 0
        while temp:
            if temp.val != 0:
                sumi += temp.val
            else:
                curr.next = ListNode(sumi)
                curr = curr.next
                sumi = 0
            temp = temp.next
        return dummy.next


        