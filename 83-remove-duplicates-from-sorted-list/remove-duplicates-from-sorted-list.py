# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()
        prev = None
        temp = head
        while temp!=None:
            if temp.val not in my_set:
                my_set.add(temp.val)
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
                temp = temp.next
        return head
        