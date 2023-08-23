# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp1=head
        lst=[]
        while temp1 is not None:
            lst.append(temp1.val)
            temp1=temp1.next
        lst.sort()
        newNode=ListNode(None)
        temp3=newNode
        for num in lst:
            if lst.count(num)==1:
                temp2=ListNode(num)
                temp2.next=None

                temp3.next=temp2
                temp3=temp3.next

        return newNode.next



