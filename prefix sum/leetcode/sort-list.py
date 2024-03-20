# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, heads: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left, right):
            dummy=ListNode(0)
            temp=dummy
            while left and right:
                if left.val <= right.val:
                    temp.next = ListNode(left.val)
                    temp = temp.next
                    left = left.next
                else:
                    temp.next=ListNode(right.val)
                    temp = temp.next
                    right = right.next
            while left:
                temp.next = ListNode(left.val)
                temp = temp.next
                left = left.next
            while right:
                temp.next=ListNode(right.val)
                temp = temp.next
                right = right.next
            return dummy.next

        def mergeSort(head):
            if not head:
                return None
            if not head.next:
                return head
            p=head
            slow=head
            fast=head
            while fast and fast.next:
                p=slow
                slow = slow.next
                fast = fast.next.next
            p.next = None
            left=mergeSort(head)
            right = mergeSort(slow)

            return merge(left, right)

        return mergeSort(heads)

                
       