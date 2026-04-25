# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        temp = head
        c = 0
        while temp:
            if temp.val in nums and (temp.next==None or temp.next.val not in nums):
                c+=1
            temp = temp.next
        return c



        