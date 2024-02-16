# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        curr=headA
        s.add(curr)
        while curr:
            curr=curr.next
            s.add(curr)
        curr2=headB
        while curr2:
            if curr2 in s:
                return curr2
            curr2=curr2.next
        if curr2 in s:
                return curr2

        return -1