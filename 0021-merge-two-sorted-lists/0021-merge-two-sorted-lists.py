# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1 = list1
        temp2 = list2
        lst = []

        
        while temp1 is not None:
            lst.append(temp1.val)
            temp1 = temp1.next

        
        while temp2 is not None:
            lst.append(temp2.val)
            temp2 = temp2.next

        lst.sort()

        
        newNode = ListNode(None)
        temp3 = newNode

        
        for num in lst:
            temp4 = ListNode(num)
            temp4.next = None

            temp3.next = temp4
            temp3 = temp3.next

        return newNode.next