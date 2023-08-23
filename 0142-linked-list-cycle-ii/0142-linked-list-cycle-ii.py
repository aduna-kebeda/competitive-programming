# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        temp1 = head
        if temp1 is None or temp1.next is None:
            return None
        lst = []
        while temp1.next is not None:
            lst.append(temp1)
            temp1 = temp1.next
            
            for node in lst:
                if node == temp1:
                    return temp1
                
        return  None
      
        