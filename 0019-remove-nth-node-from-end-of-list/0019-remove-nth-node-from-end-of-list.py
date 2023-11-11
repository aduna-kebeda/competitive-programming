# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        c=0
        while temp!=None:
            temp=temp.next
            c+=1
        temp2=head
        k=c-n
        i=0
        if c==1:
            del head
            return
        if c==n and head:
           head=head.next
           return head

        while i<k-1:
            temp2=temp2.next
            i+=1
        if temp2.next:
           temp3=temp2.next
           temp2.next=temp3.next
        return head

        