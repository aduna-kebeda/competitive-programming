# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
       
       stack=[]
       if head is None or head.next is None:
        return head
       temp=head
       
       while temp:
           if temp.val not in stack:
               stack.append(temp.val)
               temp2=temp
           else:
               temp2.next=temp.next
               

           
           temp=temp.next
       return head

        