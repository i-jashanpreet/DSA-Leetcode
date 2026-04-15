# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        end = ans

        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                end.next = head1
                end = head1
                head1 = head1.next
            else:
                end.next = head2
                end = head2
                head2 = head2.next

        if head1 != None:
            end.next = head1
        else:
            end.next = head2

        return ans.next
        