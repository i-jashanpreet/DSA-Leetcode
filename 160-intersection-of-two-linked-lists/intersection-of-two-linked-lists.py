# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # set_unique = set()
        # temp1 = headA
        # temp2 = headB
        # while temp1!=None:
        #     set_unique.add(temp1)
        #     temp1 = temp1.next
        # while temp2!=None:
        #     if temp2 in set_unique:
        #         return temp2
        #     temp2 = temp2.next
        # return None
        temp1 = headA
        temp2 = headB
        l1 = 0
        l2 = 0
        while temp1.next!=None:
            l1+=1
            temp1 = temp1.next
        while temp2.next!=None:
            l2+=1
            temp2 = temp2.next
        temp1 = headA
        temp2 = headB
        if l1>l2:
            ans = l1-l2
            for i in range(ans):
                temp1 = temp1.next
        if l2>l1:
            ans = l2-l1
            for i in range(ans):
                temp2 = temp2.next
        while temp1 and temp2:
            if temp1==temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None




        