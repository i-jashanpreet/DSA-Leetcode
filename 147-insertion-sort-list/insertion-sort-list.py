# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        head1 = ListNode(arr[0] )
        curr = head1
        for i in range(1,len(arr)):
            new = ListNode(arr[i])
            curr.next = new
            curr = new
        return head1       