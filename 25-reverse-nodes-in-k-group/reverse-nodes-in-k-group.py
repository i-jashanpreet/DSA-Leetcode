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
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        curr = head
        prevGroupTail = None
        newHead = head
        while count >= k:
            prev = None
            tail = curr   
            for i in range(k):
                front = curr.next
                curr.next = prev
                prev = curr
                curr = front
            if prevGroupTail == None:
                newHead = prev
            else:
                prevGroupTail.next = prev
            tail.next = curr
            prevGroupTail = tail
            count -= k
        return newHead