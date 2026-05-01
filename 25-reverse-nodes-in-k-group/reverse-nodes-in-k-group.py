# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prev = None
        c=0
        while temp:
            temp = temp.next
            c+=1
        if c < k:
            return head 
        temp = head
        for i in range(k):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        head.next = self.reverseKGroup(temp,k)
        return prev
