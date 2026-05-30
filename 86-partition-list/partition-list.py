# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        temp = head
        while temp:
            if temp.val < x:
                arr1.append(temp.val)
            else:
                arr2.append(temp.val)
            temp = temp.next
        arr = arr1 + arr2
        if not arr:
            return None
        head1 = ListNode(arr[0])
        temp1 = head1
        for i in range(1, len(arr)):
            new_node = ListNode(arr[i])
            temp1.next = new_node
            temp1 = temp1.next
        return head1




                    

