# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev =None
        while temp and temp.next:
            if temp.val==temp.next.val:
                y = temp.val
                while temp and temp.val==y:
                    temp = temp.next
                if prev!=None:
                    prev.next = temp
                else:
                    head = temp
            else:
                prev = temp
                temp = temp.next
        return head

        
        