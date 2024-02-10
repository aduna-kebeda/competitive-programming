class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        prev = None
        curr = head

        while curr:
            if curr.val not in s:
                s.add(curr.val)
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next

        return head
