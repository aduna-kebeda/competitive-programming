class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
      
        temp2 = head
        temp3 = head.next
        temp2.next = None

        while temp3 is not None:
            temp4 = temp3.next
            temp3.next = temp2
            temp2 = temp3
            temp3 = temp4

        return temp2