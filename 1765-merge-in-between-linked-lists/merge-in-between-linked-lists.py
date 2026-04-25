# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        for i in range(a-1):
            prev = prev.next
        after = list1
        for i in range(b+1):
            after = after.next
        first = list2
        last = list2
        while last.next!=None:
            last = last.next
        prev.next = first
        last.next = after
        return list1
        
        
        
        