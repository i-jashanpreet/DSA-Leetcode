# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_unique = set()
        temp1 = headA
        temp2 = headB
        while temp1!=None:
            set_unique.add(temp1)
            temp1 = temp1.next
        while temp2!=None:
            if temp2 in set_unique:
                return temp2
            temp2 = temp2.next
        return None


        