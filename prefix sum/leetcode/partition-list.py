# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        less_head = less = ListNode(0)
        great_head = great = ListNode(0)

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                great.next = head
                great = great.next
            head = head.next

        great.next = None
        less.next = great_head.next

        return less_head.next