# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        temp = head
        curr = head
        c = 1
        while temp.next:
            temp = temp.next
            c+=1
        temp.next = head
        k =k%c
        for i in range(c-k-1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        return new_head



        