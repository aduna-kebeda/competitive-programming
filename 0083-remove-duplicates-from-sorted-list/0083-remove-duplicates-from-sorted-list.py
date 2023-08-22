# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp1 = head
        lst = []
        
        while temp1:
            lst.append(temp1.val)
            temp1 = temp1.next
        
        lst = list(set(lst))
        lst.sort()
        
        if lst:
            new_head = ListNode(lst[0])
            temp2 = new_head
            for val in lst[1:]:
                temp2.next = ListNode(val)
                temp2 = temp2.next
            return new_head
        else:
            return None