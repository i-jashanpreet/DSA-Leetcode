# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.divide(lists)
    def merge(self,left,right):
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val<=right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next
    def divide(self,arr):
        if not arr:
            return None
        if len(arr) == 1:
            return arr[0]
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        left =self.divide(left_arr)
        right = self.divide(right_arr)
        return self.merge(left,right)
    


        


        