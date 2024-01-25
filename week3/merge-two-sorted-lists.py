class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = temp = ListNode()  

        while p1 or p2:
            v1 = p1.val if p1 else float('inf')
            v2 = p2.val if p2 else float('inf')

            if v1 < v2:
                temp.next = ListNode(v1)
                p1 = p1.next if p1 else None
            else:
                temp.next = ListNode(v2)
                p2 = p2.next if p2 else None

            temp = temp.next

        return head.next  